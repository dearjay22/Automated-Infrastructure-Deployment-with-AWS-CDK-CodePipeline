from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct


class ApiStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        lambda_fn = _lambda.Function(
            self,
            "HelloLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="handler.handler",
            code=_lambda.Code.from_asset("lambda")
        )

        api = apigw.LambdaRestApi(
            self,
            "HelloApi",
            handler=lambda_fn,
            proxy=False
        )

        api.root.add_resource("hello").add_method("GET")
