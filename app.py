#!/usr/bin/env python3

import aws_cdk as cdk

from lambda_sqs.lambda_sqs_stack import LambdaSqsStack


app = cdk.App()
LambdaSqsStack(app, "lambda-sqs")

app.synth()
