#!/usr/bin/env python3
import aws_cdk as cdk
from my_cdk_app.api_stack import ApiInfraStack
from my_cdk_app.pipeline_stack import PipelineStack

app = cdk.App()

# Deploy the Lambda + API Gateway stack first
api_stack = ApiInfraStack(app, "ApiInfraStack")

# Deploy the CodePipeline stack, pass api_stack if needed
PipelineStack(app, "PipelineStack", api_stack=api_stack)

app.synth()
