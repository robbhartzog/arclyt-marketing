# Arclyt deployment script
# Usage: .\deploy.ps1 [stack]
# Example: .\deploy.ps1 ArclytSiteStack

param(
    [string]$Stack = "ArclytSiteStack"
)

$env:CERT_ARN = "arn:aws:acm:us-east-1:711305909128:certificate/61955bc4-583c-4f31-825f-f8244e6300e7"

Write-Host "Deploying $Stack with CERT_ARN set..." -ForegroundColor Cyan

cdk deploy $Stack --require-approval never
