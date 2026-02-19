import json
import os
import boto3
from datetime import datetime
from decimal import Decimal

# Initialize AWS clients
dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses', region_name='us-east-1')

# Get environment variables
TABLE_NAME = os.environ['TABLE_NAME']
TO_EMAIL = os.environ['TO_EMAIL']  # Email address to send notifications to
FROM_EMAIL = os.environ.get('FROM_EMAIL', TO_EMAIL)  # From email (defaults to TO_EMAIL)

def lambda_handler(event, context):
    """
    Handle contact form submissions
    """
    # Handle CORS preflight
    if event.get('requestContext', {}).get('http', {}).get('method') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
            },
            'body': json.dumps({'message': 'OK'})
        }
    
    try:
        # Parse request body
        if isinstance(event.get('body'), str):
            body = json.loads(event['body'])
        else:
            body = event.get('body', {})
        
        # Extract form data
        name = body.get('name', '').strip()
        email = body.get('email', '').strip()
        company = body.get('company', '').strip()
        project_type = body.get('projectType', '')
        budget = body.get('budget', '')
        timeline = body.get('timeline', '')
        message = body.get('message', '').strip()
        
        # Validate required fields
        if not name or not email or not message:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json',
                },
                'body': json.dumps({
                    'error': 'Missing required fields: name, email, and message are required'
                })
            }
        
        # Validate email format
        if '@' not in email or '.' not in email.split('@')[1]:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json',
                },
                'body': json.dumps({
                    'error': 'Invalid email address'
                })
            }
        
        # Create submission record
        submission_id = context.request_id if context else f"sub-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{os.urandom(4).hex()}"
        timestamp = datetime.utcnow().isoformat()
        
        # Store in DynamoDB
        table = dynamodb.Table(TABLE_NAME)
        item = {
            'id': submission_id,
            'timestamp': timestamp,
            'name': name,
            'email': email,
            'company': company if company else None,
            'projectType': project_type if project_type else None,
            'budget': budget if budget else None,
            'timeline': timeline if timeline else None,
            'message': message,
        }
        
        # Remove None values
        item = {k: v for k, v in item.items() if v is not None}
        
        table.put_item(Item=item)
        
        # Send email notification
        try:
            email_subject = f"New Contact Form Submission from {name}"
            email_body = f"""
New contact form submission received:

Name: {name}
Email: {email}
Company: {company if company else 'Not provided'}
Project Type: {project_type if project_type else 'Not specified'}
Budget: {budget if budget else 'Not specified'}
Timeline: {timeline if timeline else 'Not specified'}

Message:
{message}

---
Submission ID: {submission_id}
Timestamp: {timestamp}
"""
            
            ses.send_email(
                Source=FROM_EMAIL,
                Destination={'ToAddresses': [TO_EMAIL]},
                Message={
                    'Subject': {'Data': email_subject, 'Charset': 'UTF-8'},
                    'Body': {'Text': {'Data': email_body, 'Charset': 'UTF-8'}}
                }
            )
        except Exception as e:
            # Log email error but don't fail the request
            print(f"Error sending email: {str(e)}")
        
        # Return success response
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
            'body': json.dumps({
                'message': 'Submission received successfully',
                'id': submission_id
            })
        }
    
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
            'body': json.dumps({
                'error': 'Invalid JSON in request body'
            })
        }
    except Exception as e:
        print(f"Error processing submission: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
            'body': json.dumps({
                'error': 'Internal server error'
            })
        }
