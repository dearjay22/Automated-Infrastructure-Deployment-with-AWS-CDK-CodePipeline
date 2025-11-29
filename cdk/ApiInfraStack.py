from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_dynamodb as dynamodb,
    aws_apigateway as apigw,
    RemovalPolicy
)
from constructs import Construct

class ApiInfraStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # S3 Bucket
        my_bucket = s3.Bucket(
            self,
            "Bucket9062044",
            bucket_name="jaypatel-9062044-bucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # DynamoDB Table
        my_table = dynamodb.Table(
            self,
            "Table9062044",
            table_name="JayPatel_9062044_Table",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            removal_policy=RemovalPolicy.DESTROY
        )

        # Lambda
        hello_lambda = _lambda.Function(
            self,
            "HelloLambda9062044",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "BUCKET_NAME": my_bucket.bucket_name,
                "TABLE_NAME": my_table.table_name
            }
        )

        # Grant Lambda permissions
        my_bucket.grant_read_write(hello_lambda)
        my_table.grant_read_write_data(hello_lambda)

        # API Gateway
        api = apigw.LambdaRestApi(
            self,
            "HelloApi9062044",
            handler=hello_lambda,
            proxy=False
        )

        hello_resource = api.root.add_resource("hello")
        hello_resource.add_method("GET")

        # Export references for PipelineStack
        self.bucket = my_bucket
        self.lambda_function = hello_lambda
        self.table = my_table
