import * as cdk from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as cloudfrontOrigins from 'aws-cdk-lib/aws-cloudfront-origins';
import * as acm from 'aws-cdk-lib/aws-certificatemanager';
import * as s3deploy from 'aws-cdk-lib/aws-s3-deployment';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import { Construct } from 'constructs';
import { config } from '../config';

/**
 * Main stack for Arclyt site: S3 bucket + CloudFront distribution
 */
export class ArclytSiteStack extends cdk.Stack {
  public readonly distribution: cloudfront.Distribution;
  public readonly bucket: s3.Bucket;

  constructor(scope: Construct, id: string, certArn?: string, props?: cdk.StackProps) {
    super(scope, id, {
      ...props,
      env: {
        account: process.env.CDK_DEFAULT_ACCOUNT,
        region: config.mainRegion,
      },
    });

    // Create private S3 bucket for static website
    this.bucket = new s3.Bucket(this, 'SiteBucket', {
      bucketName: `arclyt-site-${this.account}-${this.region}`,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      encryption: s3.BucketEncryption.S3_MANAGED,
      versioned: false,
      removalPolicy: cdk.RemovalPolicy.RETAIN, // Keep bucket on stack deletion
      autoDeleteObjects: false,
    });

    // Create Origin Access Control (OAC) for CloudFront
    const oac = new cloudfront.S3OriginAccessControl(this, 'SiteOAC', {
      originAccessControlName: 'arclyt-site-oac',
      description: 'OAC for Arclyt site S3 bucket',
    });

    // Get certificate from us-east-1 if provided
    let certificate: acm.ICertificate | undefined;
    if (certArn) {
      certificate = acm.Certificate.fromCertificateArn(this, 'Certificate', certArn);
    }

    // Build alternate domain names
    const alternateDomainNames = config.enableWww
      ? [config.domainName, `www.${config.domainName}`]
      : [config.domainName];

    // Create CloudFront distribution
    // Create S3 origin with OAC - use S3Origin without OAC params, then configure OAC on origin
    const s3Origin = new cloudfrontOrigins.S3Origin(this.bucket);
    
    this.distribution = new cloudfront.Distribution(this, 'SiteDistribution', {
      defaultBehavior: {
        origin: s3Origin,
        viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
        compress: true,
        allowedMethods: cloudfront.AllowedMethods.ALLOW_GET_HEAD,
        cachedMethods: cloudfront.CachedMethods.CACHE_GET_HEAD,
        cachePolicy: cloudfront.CachePolicy.CACHING_OPTIMIZED,
      },
      defaultRootObject: 'index.html',
      domainNames: certificate ? alternateDomainNames : undefined,
      certificate: certificate,
      errorResponses: [
        {
          httpStatus: 404,
          responseHttpStatus: 200,
          responsePagePath: '/index.html',
          ttl: cdk.Duration.minutes(5),
        },
        {
          httpStatus: 403,
          responseHttpStatus: 200,
          responsePagePath: '/index.html',
          ttl: cdk.Duration.minutes(5),
        },
      ],
      priceClass: cloudfront.PriceClass.PRICE_CLASS_100, // Use only North America and Europe
    });

    // Configure OAC on the distribution's origin (after creation)
    // S3Origin creates an OAI by default, so we need to override it with OAC
    const cfnDistribution = this.distribution.node.defaultChild as cloudfront.CfnDistribution;
    cfnDistribution.addPropertyOverride('DistributionConfig.Origins.0.OriginAccessControlId', oac.originAccessControlId);
    // Remove OAI configuration if it exists
    cfnDistribution.addPropertyDeletionOverride('DistributionConfig.Origins.0.S3OriginConfig.OriginAccessIdentity');

    // Update bucket policy to allow CloudFront OAC access
    this.bucket.addToResourcePolicy(
      new iam.PolicyStatement({
        sid: 'AllowCloudFrontOAC',
        effect: iam.Effect.ALLOW,
        principals: [new iam.ServicePrincipal('cloudfront.amazonaws.com')],
        actions: ['s3:GetObject'],
        resources: [this.bucket.arnForObjects('*')],
        conditions: {
          StringEquals: {
            'AWS:SourceArn': `arn:aws:cloudfront::${this.account}:distribution/${this.distribution.distributionId}`,
          },
        },
      })
    );

    // Deploy site files to S3
    new s3deploy.BucketDeployment(this, 'DeploySite', {
      sources: [s3deploy.Source.asset(config.siteSourceFolder)],
      destinationBucket: this.bucket,
      distribution: this.distribution,
      distributionPaths: ['/*'], // Invalidate all paths on deployment
    });

    // Create DynamoDB table for contact form submissions
    const contactTable = new dynamodb.Table(this, 'ContactSubmissions', {
      tableName: `arclyt-contact-submissions-${this.account}`,
      partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.RETAIN, // Keep table on stack deletion
      pointInTimeRecovery: true, // Enable PITR for data protection
    });

    // Add GSI for querying by timestamp
    contactTable.addGlobalSecondaryIndex({
      indexName: 'timestamp-index',
      partitionKey: { name: 'timestamp', type: dynamodb.AttributeType.STRING },
    });

    // Create Lambda function for contact form
    const contactHandler = new lambda.Function(this, 'ContactHandler', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'contact-handler.lambda_handler',
      code: lambda.Code.fromAsset('lambda'),
      timeout: cdk.Duration.seconds(30),
      environment: {
        TABLE_NAME: contactTable.tableName,
        TO_EMAIL: config.contactEmail,
        FROM_EMAIL: config.contactEmail,
      },
    });

    // Grant Lambda permissions
    contactTable.grantWriteData(contactHandler);
    contactHandler.addToRolePolicy(
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        actions: ['ses:SendEmail', 'ses:SendRawEmail'],
        resources: ['*'], // SES requires * for SendEmail action
      })
    );

    // Create Function URL for Lambda
    const functionUrl = contactHandler.addFunctionUrl({
      authType: lambda.FunctionUrlAuthType.NONE, // Public access (CORS handled in Lambda)
      cors: {
        allowedOrigins: [`https://${config.domainName}`, `https://www.${config.domainName}`],
        allowedMethods: [lambda.HttpMethod.POST],
        allowedHeaders: ['Content-Type'],
        maxAge: cdk.Duration.seconds(3600),
      },
    });

    // Outputs
    new cdk.CfnOutput(this, 'DistributionId', {
      value: this.distribution.distributionId,
      description: 'CloudFront Distribution ID',
    });

    new cdk.CfnOutput(this, 'DistributionDomainName', {
      value: this.distribution.distributionDomainName,
      description: 'CloudFront Distribution Domain Name',
    });

    new cdk.CfnOutput(this, 'BucketName', {
      value: this.bucket.bucketName,
      description: 'S3 Bucket Name',
    });

    new cdk.CfnOutput(this, 'SiteUrl', {
      value: certificate
        ? `https://${config.domainName}`
        : `https://${this.distribution.distributionDomainName}`,
      description: 'Site URL',
    });

    new cdk.CfnOutput(this, 'ContactFunctionUrl', {
      value: functionUrl.url,
      description: 'Lambda Function URL for contact form submissions',
    });

    new cdk.CfnOutput(this, 'ContactTableName', {
      value: contactTable.tableName,
      description: 'DynamoDB table name for contact submissions',
    });
  }
}
