# CDK GitHub → CodePipeline Example (Python)

## Overview
This repo contains a Python AWS CDK app that:
- Creates a Lambda + API Gateway + S3 bucket (AppStack)
- Creates a CodePipeline (PipelineStack) that:
  - Uses a GitHub CodeStar connection as Source
  - Uses CodeBuild to run `cdk synth`
  - Uses CloudFormation action to deploy the synthesized template

## Pre-requirements (AWS Console)
1. Create a **CodeStar Connection** (GitHub → AWS).
   - Console: Developer Tools → Connections → Create connection → GitHub.
   - Authorize, then note the connection ARN (e.g. `arn:aws:codestar-connections:us-east-1:123456789012:connection/xxxx`).
2. (Optional) Create an S3 bucket for artifacts, or allow CDK to create one.
3. Ensure your IAM user has privileges to create CodePipeline, CodeBuild, CloudFormation, Lambda, API Gateway, S3.

## Local setup
1. Clone this repo.

2. Create and activate a Python venv:
```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
```

3. Install CDK CLI (local):
```bash
   npm install -g aws-cdk
```

4. Bootstrap your AWS environment (required once):
```bash
   cdk bootstrap aws://<ACCOUNT_ID>/<REGION>
```