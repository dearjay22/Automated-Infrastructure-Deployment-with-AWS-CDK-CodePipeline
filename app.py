#!/usr/bin/env python3
import aws_cdk as cdk
from my_cdk_app.api_stack import ApiStack
from my_cdk_app.pipeline_stack import PipelineStack

app = cdk.App()

api_stack = ApiStack(app, "ApiInfraStack")

PipelineStack(
    app,
    "PipelineStack",
    api_stack=api_stack,
)

app.synth()
