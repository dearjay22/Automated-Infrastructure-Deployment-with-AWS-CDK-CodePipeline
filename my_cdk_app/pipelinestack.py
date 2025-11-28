from aws_cdk import (
    Stack,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as cp_actions,
    aws_codebuild as codebuild,
    aws_iam as iam,
)
from constructs import Construct

class PipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Artifacts
        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()

        # GitHub Source
        source_action = cp_actions.CodeStarConnectionsSourceAction(
            action_name="GitHub_Source",
            owner="dearjay22",
            repo="Automated-Infrastructure-Deployment-with-AWS-CDK-CodePipeline",
            branch="main",
            connection_arn="arn:aws:codestar-connections:us-east-1:141262319565:connection/915c367e-3387-496b-ac7b-8849d2629027",
            output=source_output
        )

        # CodeBuild Project
        project = codebuild.PipelineProject(
            self,
            "BuildProject9062044",
            build_spec=codebuild.BuildSpec.from_source_filename("buildspec.yml")
        )

        build_action = cp_actions.CodeBuildAction(
            action_name="CDK_Build",
            project=project,
            input=source_output,
            outputs=[build_output]
        )

        # CloudFormation Deploy
        deploy_action = cp_actions.CloudFormationCreateUpdateStackAction(
            action_name="Deploy_CDK",
            stack_name=api_stack.stack_name if api_stack else "ApiStack9062044",
            template_path=build_output.at_path("ApiStack9062044.template.json"),
            admin_permissions=True
        )

        # Pipeline
        pipeline = codepipeline.Pipeline(
            self,
            "Pipeline9062044",
            pipeline_name="CDK-AutoDeploy-Pipeline-9062044"
        )

        pipeline.add_stage(stage_name="Source", actions=[source_action])
        pipeline.add_stage(stage_name="Build", actions=[build_action])
        pipeline.add_stage(stage_name="Deploy", actions=[deploy_action])