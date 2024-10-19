import boto3
import json



class LambdaInvoker:
    def __init__(self):
        self.lambda_client = boto3.client('lambda')

    def ivoke_lambda(self, function_name: str) -> json:
        response = self.lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps({})
        )
        return json.loads(response['Payload'].read())
