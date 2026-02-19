# Arclyt Site Deployment Guide

This guide covers deploying the Arclyt marketing site to AWS using CDK.

## Prerequisites

1. **AWS CLI configured** with credentials:
   ```bash
   aws configure
   ```

2. **Node.js and npm** installed (v18+ recommended)

3. **AWS CDK CLI** installed and up-to-date:
   ```bash
   npm install -g aws-cdk
   # Or update if already installed
   npm update -g aws-cdk
   ```
   
   Verify version:
   ```bash
   cdk --version
   ```
   
   **Note:** If you see "schema version mismatch" errors, upgrade the CDK CLI:
   ```bash
   npm install -g aws-cdk@latest
   ```

3. **Build the site** first:
   ```bash
   npm run build
   ```
   This creates the `dist/` folder with static files.

## Initial Setup

### 1. Install Infrastructure Dependencies

```bash
npm run infra:install
```

### 2. Bootstrap CDK (First Time Only)

CDK needs to be bootstrapped in us-east-1:
- All resources (S3, CloudFront, ACM certificate) are in `us-east-1`

```bash
npm run infra:bootstrap
```

Or manually:
```bash
cd infra
cdk bootstrap --region us-east-1
```

**Note:** CDK bootstrap will automatically detect your AWS account ID from your configured credentials.

## Deployment Steps

### Step 1: Deploy Certificate Stack

Deploy the certificate stack first to create the ACM certificate:

```bash
cd infra
npm run build
cdk deploy ArclytCertStack
```

**Output:** The stack will output the certificate ARN and DNS validation instructions.

### Step 2: Get DNS Validation Records

After the certificate stack deploys, the stack outputs will include:
- **CertificateArn**: The certificate ARN
- **ValidationRecords**: A JSON array of DNS validation CNAME records

**Get validation records from stack output:**

```bash
aws cloudformation describe-stacks \
  --stack-name arclyt-cert \
  --region us-east-1 \
  --query 'Stacks[0].Outputs[?OutputKey==`ValidationRecords`].OutputValue' \
  --output text
```

This will output JSON like:
```json
[
  {
    "DomainName": "arclyt.io",
    "Name": "_abc123.arclyt.io.",
    "Value": "_xyz789.acm-validations.aws.",
    "Type": "CNAME"
  },
  {
    "DomainName": "www.arclyt.io",
    "Name": "_def456.www.arclyt.io.",
    "Value": "_uvw012.acm-validations.aws.",
    "Type": "CNAME"
  }
]
```

**Alternative: Get from AWS Console**
1. Go to AWS Certificate Manager (ACM) in `us-east-1`
2. Find the certificate for `arclyt.io`
3. View the DNS validation records
4. Copy the CNAME records (Name and Value)

### Step 3: Add DNS Validation Records to Route53

**Manually add CNAME records in Route53:**

1. Go to Route53 → Hosted Zones → `arclyt.io`
2. Click "Create record"
3. For each validation record from the JSON output:
   - **Record name:** Use the `Name` field (e.g., `_abc123.arclyt.io` - remove trailing dot if present)
   - **Record type:** CNAME
   - **Value:** Use the `Value` field (e.g., `_xyz789.acm-validations.aws.` - include trailing dot)
   - **TTL:** 300 (or default)
   - Click "Create records"

4. Repeat for each domain in the validation records array

**Important:** 
- The record name should match the `Name` field from the JSON (you may need to remove the trailing dot)
- The value should include the trailing dot if present in the JSON
- DNS propagation can take 5-30 minutes
- You need one CNAME record per domain (apex and www if enabled)

### Step 4: Wait for Certificate Validation

Monitor certificate status:

```bash
aws acm describe-certificate \
  --certificate-arn <CERTIFICATE_ARN> \
  --region us-east-1 \
  --query 'Certificate.Status' \
  --output text
```

Wait until status is `ISSUED` (this can take 5-30 minutes after DNS records are added).

**Check in Console:**
- Go to ACM in `us-east-1`
- Certificate status should show "Issued" (green checkmark)

### Step 5: Get Certificate ARN and Set Environment Variable

Get the certificate ARN from the stack output:

```bash
aws cloudformation describe-stacks \
  --stack-name arclyt-cert \
  --region us-east-1 \
  --query 'Stacks[0].Outputs[?OutputKey==`CertificateArn`].OutputValue' \
  --output text
```

Or get it from the CDK output after deployment (it's also displayed in the terminal).

Set the certificate ARN as an environment variable:

**Linux/Mac:**
```bash
export CERT_ARN=arn:aws:acm:us-east-1:YOUR_ACCOUNT:certificate/YOUR_CERT_ID
```

**Windows PowerShell:**
```powershell
$env:CERT_ARN="arn:aws:acm:us-east-1:YOUR_ACCOUNT:certificate/YOUR_CERT_ID"
```

**Windows CMD:**
```cmd
set CERT_ARN=arn:aws:acm:us-east-1:YOUR_ACCOUNT:certificate/YOUR_CERT_ID
```

**Verify it's set:**
```bash
echo $CERT_ARN  # Linux/Mac
echo $env:CERT_ARN  # PowerShell
```

### Step 6: Deploy Site Stack

Make sure the `CERT_ARN` environment variable is set, then deploy:

```bash
cd infra
npm run build
cdk deploy ArclytSiteStack
```

**Note:** If you didn't set the environment variable, the site will deploy without a custom domain. You can update it later by setting `CERT_ARN` and redeploying.

**Output:** The stack will output:
- CloudFront Distribution ID
- CloudFront Distribution Domain Name
- S3 Bucket Name
- Site URL

### Step 7: Create Route53 Alias Records

**Manually create Route53 A/AAAA alias records:**

1. Go to Route53 → Hosted Zones → `arclyt.io`
2. Click "Create record"
3. For apex domain (`arclyt.io`):
   - **Record name:** Leave blank (or `@`)
   - **Record type:** A
   - **Alias:** Yes
   - **Route traffic to:** Alias to CloudFront distribution
   - **Distribution:** Select your CloudFront distribution
   - Click "Create records"

4. For www subdomain (if enabled):
   - **Record name:** `www`
   - **Record type:** A
   - **Alias:** Yes
   - **Route traffic to:** Alias to CloudFront distribution
   - **Distribution:** Select your CloudFront distribution
   - Click "Create records"

**Note:** You can also create AAAA records for IPv6 support (same process, select AAAA type).

### Step 8: Wait for DNS Propagation

DNS changes can take 5-60 minutes to propagate globally. Test with:

```bash
dig arclyt.io
# or
nslookup arclyt.io
```

## Updating the Site

After making changes to the site:

1. **Build the site:**
   ```bash
   npm run build
   ```

2. **Deploy infrastructure:**
   ```bash
   npm run infra:deploy
   ```

   Or deploy just the site stack:
   ```bash
   cd infra
   npm run build
   cdk deploy ArclytSiteStack
   ```

The `BucketDeployment` construct will automatically:
- Upload new files to S3
- Invalidate CloudFront cache for changed files

## Useful Commands

```bash
# Install infrastructure dependencies
npm run infra:install

# Bootstrap CDK (first time only)
npm run infra:bootstrap

# Build TypeScript
cd infra && npm run build

# Synthesize CloudFormation templates
cd infra && cdk synth

# Deploy all stacks
npm run infra:deploy

# Deploy specific stack
cd infra && cdk deploy ArclytCertStack
cd infra && cdk deploy ArclytSiteStack

# View differences before deploying
cd infra && cdk diff

# Destroy stacks (careful!)
cd infra && cdk destroy ArclytSiteStack
cd infra && cdk destroy ArclytCertStack
```

## Troubleshooting

### Certificate Not Validating

- Verify DNS validation CNAME records are correctly added to Route53
- Check record names match exactly (including subdomain prefixes)
- Wait longer (can take up to 30 minutes)
- Verify Route53 hosted zone is for the correct domain

### CloudFront Not Using Certificate

- Ensure certificate is in `us-east-1` region
- Certificate must be in `ISSUED` status
- Verify certificate ARN is correctly passed to site stack
- Check CloudFront distribution has the correct alternate domain names

### Site Not Loading

- Check CloudFront distribution status (should be "Deployed")
- Verify Route53 alias records point to CloudFront distribution
- Check S3 bucket has files (via AWS Console)
- Test CloudFront domain directly: `https://<distribution-id>.cloudfront.net`

### Build Errors

- Ensure `dist/` folder exists (run `npm run build` first)
- Check `infra/config.ts` has correct `siteSourceFolder` path
- Verify all dependencies installed: `npm run infra:install`

## Configuration

Edit `infra/config.ts` to change:
- Domain name
- Enable/disable www subdomain
- AWS regions
- Site source folder path

## Contact Form Setup

The contact form uses a Lambda Function URL with DynamoDB storage and SES email notifications.

### Prerequisites for Contact Form

1. **SES Email Verification** (required before deployment):
   - Go to AWS SES Console in `us-east-1`
   - Verify the email address you want to receive submissions at (e.g., `hello@arclyt.io`)
   - If your AWS account is in SES sandbox mode, you can only send to verified emails
   - To send to any email, request production access in SES

2. **Set Contact Email** (optional):
   ```bash
   export CONTACT_EMAIL="hello@arclyt.io"
   ```
   Or set it in your environment before running `cdk deploy`.

### After Deployment

1. **Get the Lambda Function URL** from the stack outputs:
   ```bash
   aws cloudformation describe-stacks \
     --stack-name arclyt-site \
     --region us-east-1 \
     --query 'Stacks[0].Outputs[?OutputKey==`ContactFunctionUrl`].OutputValue' \
     --output text
   ```

2. **Create `.env` file** in the project root:
   ```bash
   echo "VITE_CONTACT_API_URL=https://your-lambda-url.lambda-url.us-east-1.on.aws" > .env
   ```

3. **Rebuild and redeploy** the site:
   ```bash
   npm run build
   cd infra && npm run build && cdk deploy ArclytSiteStack --require-approval never
   ```

### Contact Form Features

- **DynamoDB Storage**: All submissions are stored in DynamoDB table `arclyt-contact-submissions-{account-id}`
- **Email Notifications**: Submissions are emailed to the configured address
- **CORS Enabled**: Function URL is configured for CORS from your domain
- **Spam Protection**: Form includes honeypot and time-to-submit checks

### Viewing Submissions

You can query submissions in DynamoDB:
```bash
aws dynamodb scan \
  --table-name arclyt-contact-submissions-{your-account-id} \
  --region us-east-1
```

Or use the AWS Console: DynamoDB → Tables → `arclyt-contact-submissions-{account-id}`

## Security Notes

- S3 bucket is private (Block Public Access enabled)
- CloudFront uses Origin Access Control (OAC) to access S3
- HTTPS enforced (HTTP redirects to HTTPS)
- Certificate validation required before custom domain works
- Lambda Function URL is public but includes CORS restrictions
- DynamoDB table uses pay-per-request billing (no minimum charges)
