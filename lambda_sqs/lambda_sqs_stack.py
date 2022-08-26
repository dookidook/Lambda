from constructs import Construct
from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as _aws_lambda_event_sources,
    Stack,
    Duration
)


class LambdaSqsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        #Making SQLS Queue
        queue = sqs.Queue(
            self, "LambdaSqsQueue",
            visibility_timeout=Duration.seconds(300),
        )
    # making Lambda
        sqs_lambda=_lambda.Function(self, 'sqltrigger',
            handler='lambda_handler.handler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.asset('lambda')
        )

        sqs_event_source= _aws_lambda_event_sources.SqsEventSource(queue)
    #Link SQS event source to the Lambda funciton
        sqs_lambda.add_event_source(sqs_event_source)