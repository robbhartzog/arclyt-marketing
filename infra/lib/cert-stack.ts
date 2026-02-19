import * as cdk from 'aws-cdk-lib';
import * as acm from 'aws-cdk-lib/aws-certificatemanager';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as customResources from 'aws-cdk-lib/custom-resources';
import { Construct } from 'constructs';
import { config } from '../config';

/**
 * Stack for ACM certificate in us-east-1 (required for CloudFront)
 * Uses a custom resource to create the certificate and output DNS validation records
 * that must be manually added to Route53
 */
export class ArclytCertStack extends cdk.Stack {
  public readonly certificateArn: string;

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, {
      ...props,
      env: {
        account: process.env.CDK_DEFAULT_ACCOUNT,
        region: config.certRegion, // Must be us-east-1 for CloudFront
      },
    });

    // Lambda function to create certificate and return validation records
    const certHandler = new lambda.Function(this, 'CertHandler', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromInline(`
import boto3
import cfnresponse
import json as json_module

def handler(event, context):
    import json as json_module
    acm = boto3.client('acm', region_name='us-east-1')
    
    # Initialize response data with ValidationRecords to ensure it's always present
    response_data = {
        'CertificateArn': '',
        'ValidationRecords': '[]'
    }
    
    try:
        if event['RequestType'] == 'Create' or event['RequestType'] == 'Update':
            domain_name = event['ResourceProperties']['DomainName']
            subject_alt_names = event['ResourceProperties'].get('SubjectAlternativeNames', [])
            
            # Request certificate
            response = acm.request_certificate(
                DomainName=domain_name,
                SubjectAlternativeNames=subject_alt_names if subject_alt_names else None,
                ValidationMethod='DNS'
            )
            
            cert_arn = response['CertificateArn']
            
            # Get validation records - may need to retry as they're not immediately available
            import time
            max_retries = 10
            retry_delay = 2
            validation_records = []
            
            try:
                for attempt in range(max_retries):
                    try:
                        cert_details = acm.describe_certificate(CertificateArn=cert_arn)
                        validation_options = cert_details['Certificate']['DomainValidationOptions']
                        
                        validation_records = []
                        for option in validation_options:
                            if 'ResourceRecord' in option:
                                validation_records.append({
                                    'DomainName': option['DomainName'],
                                    'Name': option['ResourceRecord']['Name'],
                                    'Value': option['ResourceRecord']['Value'],
                                    'Type': option['ResourceRecord']['Type']
                                })
                        
                        if validation_records:
                            break
                    except Exception as e:
                        print(f"Attempt {attempt + 1} failed: {str(e)}")
                        if attempt == max_retries - 1:
                            raise
                    
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
            except Exception as e:
                print(f"Failed to get validation records: {str(e)}")
                validation_records = []  # Continue with empty list
            
            # Always include ValidationRecords in response, even if empty
            response_data['CertificateArn'] = cert_arn
            response_data['ValidationRecords'] = json_module.dumps(validation_records)
            print(f"Sending response with CertificateArn: {cert_arn}, ValidationRecords: {len(validation_records)} records")
            cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data, cert_arn)
            
        elif event['RequestType'] == 'Delete':
            cert_arn = event['PhysicalResourceId']
            try:
                acm.delete_certificate(CertificateArn=cert_arn)
            except:
                pass  # Certificate might already be deleted
            cfnresponse.send(event, context, cfnresponse.SUCCESS, {}, cert_arn)
            
    except Exception as e:
        import traceback
        print(f"Error: {str(e)}")
        print(traceback.format_exc())
        # Even on failure, include ValidationRecords to satisfy CloudFormation
        error_response = {
            'Error': str(e),
            'CertificateArn': response_data.get('CertificateArn', ''),
            'ValidationRecords': response_data.get('ValidationRecords', '[]')
        }
        cfnresponse.send(event, context, cfnresponse.FAILED, error_response, response_data.get('CertificateArn', ''))
`),
      timeout: cdk.Duration.minutes(5),
    });

    // Grant permissions
    certHandler.addToRolePolicy(
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        actions: [
          'acm:RequestCertificate',
          'acm:DescribeCertificate',
          'acm:DeleteCertificate',
          'acm:ListCertificates',
        ],
        resources: ['*'],
      })
    );

    // Domain names
    const subjectAltNames = config.enableWww ? [`www.${config.domainName}`] : [];

    // Custom resource
    const certResource = new customResources.Provider(this, 'CertProvider', {
      onEventHandler: certHandler,
    });

    const cert = new cdk.CustomResource(this, 'Certificate', {
      serviceToken: certResource.serviceToken,
      properties: {
        DomainName: config.domainName,
        SubjectAlternativeNames: subjectAltNames,
      },
    });

    this.certificateArn = cert.getAttString('CertificateArn');
    // Get ValidationRecords as string (may be empty JSON array if not available yet)
    // Use getAtt with a fallback to handle cases where it might not be available
    let validationRecords: string;
    try {
      validationRecords = cert.getAttString('ValidationRecords');
    } catch (e) {
      validationRecords = '[]'; // Fallback to empty array
    }

    // Output certificate ARN
    new cdk.CfnOutput(this, 'CertificateArn', {
      value: this.certificateArn,
      description: 'ACM Certificate ARN (us-east-1)',
      exportName: 'ArclytCertArn',
    });

    // Output validation records
    new cdk.CfnOutput(this, 'ValidationRecords', {
      value: validationRecords || '[]',
      description: 'DNS validation CNAME records (JSON) - Add these to Route53. If empty, check AWS Console.',
    });

    new cdk.CfnOutput(this, 'ValidationInstructions', {
      value: `Parse the ValidationRecords JSON output above. For each record, add a CNAME in Route53:
- Name: Use the 'Name' field (e.g., _abc123.arclyt.io)
- Value: Use the 'Value' field (e.g., _xyz789.acm-validations.aws.)
Wait 5-30 minutes for validation, then set CERT_ARN=${this.certificateArn} and deploy site stack.`,
      description: 'DNS Validation Instructions',
    });
  }
}
