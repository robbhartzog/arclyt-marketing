#!/usr/bin/env node
import 'source-map-support/register';
import * as path from 'path';
import * as dotenv from 'dotenv';
import * as cdk from 'aws-cdk-lib';

dotenv.config({ path: path.resolve(__dirname, '../../.env') });
import { ArclytCertStack } from '../lib/cert-stack';
import { ArclytSiteStack } from '../lib/site-stack';
import { config } from '../config';

const app = new cdk.App();

// Certificate stack in us-east-1 (required for CloudFront)
const certStack = new ArclytCertStack(app, 'ArclytCertStack', {
  stackName: 'arclyt-cert',
  description: 'ACM Certificate for Arclyt site (us-east-1)',
});

// Main site stack in us-east-1
// Note: For initial deployment:
// 1. Deploy cert stack first: cdk deploy ArclytCertStack
// 2. Get certificate ARN from stack output
// 3. Add DNS validation records to Route53 (from stack output)
// 4. Wait for certificate validation (5-30 minutes)
// 5. Set CERT_ARN environment variable and deploy site stack
//
// To get cert ARN after cert stack deployment:
// aws cloudformation describe-stacks --stack-name arclyt-cert --region us-east-1 --query 'Stacks[0].Outputs[?OutputKey==`CertificateArn`].OutputValue' --output text
//
// Then set environment variable:
// export CERT_ARN=arn:aws:acm:us-east-1:ACCOUNT:certificate/ID
// Or on Windows: $env:CERT_ARN="arn:aws:acm:us-east-1:ACCOUNT:certificate/ID"
const certArn = process.env.CERT_ARN; // Set via: $env:CERT_ARN="arn:aws:acm:us-east-1:ACCOUNT:certificate/ID"
if (!certArn) {
  console.warn('\x1b[33m⚠ WARNING: CERT_ARN not set — deploying without SSL certificate and custom domain!\x1b[0m');
}

const siteStack = new ArclytSiteStack(app, 'ArclytSiteStack', certArn, {
  stackName: 'arclyt-site',
  description: 'Arclyt marketing site: S3 + CloudFront (us-east-1)',
});

// Add dependency: site stack depends on cert stack
siteStack.addDependency(certStack);
