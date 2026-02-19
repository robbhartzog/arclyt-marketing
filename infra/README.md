# Arclyt Infrastructure

AWS CDK v2 infrastructure for deploying the Arclyt marketing site.

## Stacks

- **ArclytCertStack** (us-east-1): ACM certificate for CloudFront
- **ArclytSiteStack** (us-east-1): S3 bucket + CloudFront distribution

## Configuration

Edit `config.ts` to change:
- Domain name
- Enable/disable www subdomain
- Regions
- Site source folder
