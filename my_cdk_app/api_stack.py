from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct

class ApiInfraStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Lambda function
        hello_lambda = _lambda.Function(
            self,
            "HelloLambda",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),
        )

        # API Gateway
        api = apigw.LambdaRestApi(
            self,
            "HelloApi",
            handler=hello_lambda,
            proxy=False
        )

        # Add GET /hello endpoint
        hello_resource = api.root.add_resource("hello")
        hello_resource.add_method("GET")  # GET /hello
