from aws_cdk import (
    Stack,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as cp_actions,
    aws_codebuild as codebuild,
)
from constructs import Construct

class PipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, api_stack=None, **kwargs):
        super().__init__(scope, id, **kwargs)

        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()

        # GitHub Source
        source_action = cp_actions.CodeStarConnectionsSourceAction(
            action_name="GitHub_Source",
            owner="dearjay22",
            repo="Automated-Infrastructure-Deployment-with-AWS-CDK-CodePipeline",
            branch="main",
            connection_arn="arn:aws:codeconnections:us-east-2:141262319565:connection/54c58779-1895-4f91-aacf-89090eb8d3f6",
            output=source_output,
        )

        # CodeBuild Project
        project = codebuild.PipelineProject(
            self,
            "BuildProject",
            build_spec=codebuild.BuildSpec.from_source_filename("buildspec.yml"),
        )

        build_action = cp_actions.CodeBuildAction(
            action_name="CDK_Build",
            project=project,
            input=source_output,
            outputs=[build_output],
        )

        # CloudFormation Deploy
        deploy_action = cp_actions.CloudFormationCreateUpdateStackAction(
            action_name="Deploy_CDK",
            stack_name="ApiInfraStack",
            template_path=build_output.at_path("ApiInfraStack.template.json"),
            admin_permissions=True,
        )

        pipeline = codepipeline.Pipeline(
            self,
            "Pipeline",
            pipeline_name="CDK-AutoDeploy-Pipeline",
        )

        pipeline.add_stage(stage_name="Source", actions=[source_action])
        pipeline.add_stage(stage_name="Build", actions=[build_action])
        pipeline.add_stage(stage_name="Deploy", actions=[deploy_action])
