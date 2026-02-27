import json
import os
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
ses       = boto3.client('ses', region_name='us-east-1')

TABLE_NAME = os.environ['TABLE_NAME']
TO_EMAIL   = os.environ['TO_EMAIL']
FROM_EMAIL = os.environ.get('FROM_EMAIL', TO_EMAIL)
DOMAIN     = os.environ.get('DOMAIN', 'arclyt.io')


# ── Email templates ────────────────────────────────────────────────────────────

def _email_card_open(header_right_html: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="color-scheme" content="dark">
  <meta name="supported-color-schemes" content="dark">
</head>
<body style="margin:0;padding:0;background-color:#0a0f1a;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" border="0"
       style="background-color:#0a0f1a;padding:40px 20px;">
  <tr>
    <td align="center">

      <!-- Card -->
      <table width="100%" cellpadding="0" cellspacing="0" border="0"
             style="max-width:580px;background-color:#0d1117;border:1px solid #30363d;border-radius:12px;overflow:hidden;">

        <!-- Cobalt top accent -->
        <tr>
          <td height="3" style="background-color:#2f81f7;font-size:0;line-height:0;">&nbsp;</td>
        </tr>

        <!-- Header -->
        <tr>
          <td style="padding:26px 36px 22px;border-bottom:1px solid #21262d;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td>
                  <span style="font-size:13px;font-weight:700;letter-spacing:3.5px;
                               text-transform:uppercase;color:#f0f4ff;">ARCLYT</span>
                </td>
                <td align="right">
                  {header_right_html}
                </td>
              </tr>
            </table>
          </td>
        </tr>"""


def _email_card_footer() -> str:
    return f"""        <!-- Footer -->
        <tr>
          <td style="padding:18px 36px;border-top:1px solid #21262d;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td>
                  <span style="font-size:11px;color:rgba(240,244,255,0.28);">
                    Arclyt &nbsp;&middot;&nbsp; AWS Certified Cloud Engineering
                  </span>
                </td>
                <td align="right">
                  <a href="https://{DOMAIN}"
                     style="font-size:11px;color:rgba(47,129,247,0.60);text-decoration:none;">
                    {DOMAIN}
                  </a>
                </td>
              </tr>
            </table>
          </td>
        </tr>

      </table>
    </td>
  </tr>
</table>
</body>
</html>"""


def build_user_confirmation_html(name: str, scheduled_date: str, scheduled_time: str) -> str:
    first_name = name.split()[0] if name else 'there'

    header_right = '<span style="font-size:11px;color:rgba(240,244,255,0.35);letter-spacing:0.08em;text-transform:uppercase;">Strategy Call</span>'

    body = f"""
        <!-- Body -->
        <tr>
          <td style="padding:36px 36px 32px;">

            <!-- Check icon -->
            <table cellpadding="0" cellspacing="0" border="0" style="margin-bottom:22px;">
              <tr>
                <td width="46" height="46"
                    style="width:46px;height:46px;background-color:rgba(47,129,247,0.10);
                           border:1px solid rgba(47,129,247,0.35);border-radius:50%;
                           text-align:center;vertical-align:middle;">
                  <span style="font-size:18px;color:#2f81f7;">&#10003;</span>
                </td>
              </tr>
            </table>

            <h1 style="margin:0 0 8px;font-size:21px;font-weight:600;
                       color:#f0f4ff;letter-spacing:-0.01em;">
              You're confirmed, {first_name}.
            </h1>
            <p style="margin:0 0 30px;font-size:14px;color:rgba(240,244,255,0.50);line-height:1.65;">
              Your 30-minute strategy call has been scheduled. We look forward to
              discussing your architecture and migration goals.
            </p>

            <!-- Slot box -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0"
                   style="background-color:rgba(47,129,247,0.06);
                          border:1px solid rgba(47,129,247,0.28);
                          border-radius:8px;margin-bottom:28px;">
              <tr>
                <td style="padding:14px 22px 12px;
                           border-bottom:1px solid rgba(47,129,247,0.15);">
                  <span style="font-size:10px;letter-spacing:0.12em;text-transform:uppercase;
                               color:rgba(47,129,247,0.70);">Confirmed Session</span>
                </td>
              </tr>
              <tr>
                <td style="padding:18px 22px;">
                  <table width="100%" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                      <td style="padding-bottom:12px;">
                        <span style="display:block;font-size:10px;text-transform:uppercase;
                                     letter-spacing:0.09em;color:rgba(240,244,255,0.32);
                                     margin-bottom:4px;">Date</span>
                        <span style="font-size:15px;font-weight:600;color:#f0f4ff;
                                     font-family:'Courier New',Courier,monospace;">
                          {scheduled_date}
                        </span>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <span style="display:block;font-size:10px;text-transform:uppercase;
                                     letter-spacing:0.09em;color:rgba(240,244,255,0.32);
                                     margin-bottom:4px;">Time</span>
                        <span style="font-size:15px;font-weight:600;color:#f0f4ff;
                                     font-family:'Courier New',Courier,monospace;">
                          {scheduled_time} EST
                        </span>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>

            <p style="margin:0;font-size:13px;color:rgba(240,244,255,0.40);line-height:1.65;">
              Need to reschedule? Simply reply to this email and we will find
              a time that works.
            </p>

          </td>
        </tr>
"""

    return _email_card_open(header_right) + body + _email_card_footer()


def build_user_confirmation_text(name: str, scheduled_date: str, scheduled_time: str) -> str:
    first_name = name.split()[0] if name else 'there'
    return f"""ARCLYT — Strategy Call Confirmed

You're confirmed, {first_name}.

Your 30-minute strategy call has been scheduled.

  Date: {scheduled_date}
  Time: {scheduled_time} EST

We look forward to discussing your architecture and migration goals.

Need to reschedule? Simply reply to this email.

—
Arclyt · AWS Certified Cloud Engineering
https://{DOMAIN}
"""


def build_admin_notification_html(
    name: str,
    email: str,
    company: str,
    tech_stack: str,
    scheduled_date: str,
    scheduled_time: str,
    submission_id: str,
    timestamp: str,
) -> str:

    header_right = """<span style="display:inline-block;padding:3px 10px;
                        border:1px solid rgba(47,129,247,0.40);border-radius:99px;
                        font-size:11px;color:rgba(47,129,247,0.85);
                        letter-spacing:0.05em;">New Booking</span>"""

    company_row = ""
    if company:
        company_row = f"""
                <tr>
                  <td style="padding:11px 0;border-bottom:1px solid #21262d;">
                    <span style="display:block;font-size:10px;text-transform:uppercase;
                                 letter-spacing:0.09em;color:rgba(240,244,255,0.32);
                                 margin-bottom:4px;">Company</span>
                    <span style="font-size:14px;color:#f0f4ff;">{company}</span>
                  </td>
                </tr>"""

    tech_stack_section = ""
    if tech_stack:
        tech_stack_section = f"""
              <tr>
                <td style="padding-top:20px;">
                  <span style="display:block;font-size:10px;text-transform:uppercase;
                               letter-spacing:0.09em;color:rgba(47,129,247,0.70);
                               margin-bottom:10px;">Current Tech Stack</span>
                  <table width="100%" cellpadding="0" cellspacing="0" border="0"
                         style="background-color:#0a0f1a;border:1px solid #30363d;
                                border-radius:6px;">
                    <tr>
                      <td style="padding:13px 16px;
                                 font-family:'Courier New',Courier,monospace;
                                 font-size:13px;color:rgba(240,244,255,0.72);
                                 line-height:1.65;">
                        {tech_stack}
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>"""

    body = f"""
        <!-- Date/time bar -->
        <tr>
          <td style="padding:14px 36px;background-color:rgba(47,129,247,0.06);
                     border-bottom:1px solid rgba(47,129,247,0.15);">
            <span style="font-size:13px;font-weight:600;color:rgba(47,129,247,0.90);
                         font-family:'Courier New',Courier,monospace;">
              {scheduled_date} &nbsp;&middot;&nbsp; {scheduled_time} EST
            </span>
          </td>
        </tr>

        <!-- Body -->
        <tr>
          <td style="padding:28px 36px 24px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0">

              <!-- Name -->
              <tr>
                <td style="padding:11px 0;border-bottom:1px solid #21262d;">
                  <span style="display:block;font-size:10px;text-transform:uppercase;
                               letter-spacing:0.09em;color:rgba(240,244,255,0.32);
                               margin-bottom:4px;">Name</span>
                  <span style="font-size:14px;font-weight:600;color:#f0f4ff;">{name}</span>
                </td>
              </tr>

              <!-- Email -->
              <tr>
                <td style="padding:11px 0;border-bottom:1px solid #21262d;">
                  <span style="display:block;font-size:10px;text-transform:uppercase;
                               letter-spacing:0.09em;color:rgba(240,244,255,0.32);
                               margin-bottom:4px;">Email</span>
                  <a href="mailto:{email}"
                     style="font-size:14px;color:rgba(47,129,247,0.85);text-decoration:none;">
                    {email}
                  </a>
                </td>
              </tr>
              {company_row}
              {tech_stack_section}

            </table>
          </td>
        </tr>

        <!-- Meta footer -->
        <tr>
          <td style="padding:14px 36px;border-top:1px solid #21262d;
                     background-color:rgba(255,255,255,0.02);">
            <span style="font-size:10px;color:rgba(240,244,255,0.22);
                         font-family:'Courier New',Courier,monospace;">
              id: {submission_id} &nbsp;&middot;&nbsp; {timestamp}
            </span>
          </td>
        </tr>
"""

    return _email_card_open(header_right) + body + _email_card_footer()


def build_admin_notification_text(
    name: str,
    email: str,
    company: str,
    tech_stack: str,
    scheduled_date: str,
    scheduled_time: str,
    submission_id: str,
    timestamp: str,
) -> str:
    lines = [
        "ARCLYT — New Strategy Call Booking",
        "",
        f"  Date:    {scheduled_date}",
        f"  Time:    {scheduled_time} EST",
        f"  Status:  Scheduled",
        "",
        f"  Name:    {name}",
        f"  Email:   {email}",
    ]
    if company:
        lines.append(f"  Company: {company}")
    if tech_stack:
        lines += ["", "  Current Tech Stack:", f"  {tech_stack}"]
    lines += ["", f"  id: {submission_id}", f"  {timestamp}"]
    return "\n".join(lines)


# ── Lambda handler ─────────────────────────────────────────────────────────────

def lambda_handler(event, context):
    """
    Handle /schedule-call POST requests.
    CORS headers are managed by the Lambda Function URL config.
    """
    try:
        # Parse body
        body = event.get('body', {})
        if isinstance(body, str):
            body = json.loads(body)

        name           = body.get('name', '').strip()
        email          = body.get('email', '').strip()
        company        = body.get('company', '').strip()
        tech_stack     = body.get('techStack', '').strip()
        scheduled_date = body.get('scheduledDate', '').strip()
        scheduled_time = body.get('scheduledTime', '').strip()

        # Validate required fields
        missing = [f for f, v in {
            'name': name,
            'email': email,
            'scheduledDate': scheduled_date,
            'scheduledTime': scheduled_time,
        }.items() if not v]

        if missing:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({
                    'error': f"Missing required fields: {', '.join(missing)}"
                }),
            }

        if '@' not in email or '.' not in email.split('@')[-1]:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Invalid email address'}),
            }

        # Build and store DynamoDB record
        submission_id = context.aws_request_id
        timestamp     = datetime.utcnow().isoformat()

        table = dynamodb.Table(TABLE_NAME)
        item  = {k: v for k, v in {
            'id':            submission_id,
            'timestamp':     timestamp,
            'type':          'schedule-call',
            'status':        'Scheduled',
            'name':          name,
            'email':         email,
            'company':       company  or None,
            'techStack':     tech_stack or None,
            'scheduledDate': scheduled_date,
            'scheduledTime': scheduled_time,
        }.items() if v is not None}

        table.put_item(Item=item)

        # Send user confirmation email
        try:
            ses.send_email(
                Source=f"Arclyt <{FROM_EMAIL}>",
                Destination={'ToAddresses': [email]},
                ReplyToAddresses=[TO_EMAIL],
                Message={
                    'Subject': {
                        'Data': f"Your strategy call is confirmed — Arclyt",
                        'Charset': 'UTF-8',
                    },
                    'Body': {
                        'Text': {
                            'Data': build_user_confirmation_text(
                                name, scheduled_date, scheduled_time
                            ),
                            'Charset': 'UTF-8',
                        },
                        'Html': {
                            'Data': build_user_confirmation_html(
                                name, scheduled_date, scheduled_time
                            ),
                            'Charset': 'UTF-8',
                        },
                    },
                },
            )
        except Exception as e:
            print(f"Error sending user confirmation email: {e}")

        # Send admin notification email
        try:
            ses.send_email(
                Source=f"Arclyt Bookings <{FROM_EMAIL}>",
                Destination={'ToAddresses': [TO_EMAIL]},
                ReplyToAddresses=[email],
                Message={
                    'Subject': {
                        'Data': f"Strategy Call: {name} — {scheduled_date} {scheduled_time}",
                        'Charset': 'UTF-8',
                    },
                    'Body': {
                        'Text': {
                            'Data': build_admin_notification_text(
                                name, email, company, tech_stack,
                                scheduled_date, scheduled_time,
                                submission_id, timestamp,
                            ),
                            'Charset': 'UTF-8',
                        },
                        'Html': {
                            'Data': build_admin_notification_html(
                                name, email, company, tech_stack,
                                scheduled_date, scheduled_time,
                                submission_id, timestamp,
                            ),
                            'Charset': 'UTF-8',
                        },
                    },
                },
            )
        except Exception as e:
            print(f"Error sending admin notification email: {e}")

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'message': 'Strategy call scheduled successfully',
                'id': submission_id,
            }),
        }

    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Invalid JSON in request body'}),
        }
    except Exception as e:
        print(f"Error processing schedule request: {e}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Internal server error'}),
        }
