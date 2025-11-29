#!/usr/bin/env python3
import aws_cdk as cdk
from ApiInfraStack import ApiInfraStack
from PipelineStack import PipelineStack

app = cdk.App()

env = cdk.Environment(
    account=app.node.try_get_context("aws_account"),
    region=app.node.try_get_context("aws_region")
)

# Deploy Lambda + S3 + DynamoDB stack
api_stack = ApiInfraStack(app, "ApiInfraStack", env=env)

# Deploy Pipeline stack
PipelineStack(app, "PipelineStack", env=env, api_stack=api_stack)

app.synth()
