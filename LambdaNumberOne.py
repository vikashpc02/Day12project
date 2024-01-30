import json
import boto3

lambdaClient = boto3.client('lambda')

def lambda_handler(event, context):
    input = {
        'agentNumber' : 12345,
        'message' : 'A secret message from lambda number 1. Over!!'
    }
    
    response = lambdaClient.invoke(
        FunctionName='arn:aws:lambda:ap-south-1:539499389206:function:Lambdanumbertwo',
        InvocationType='RequestResponse',
        Payload=json.dumps(input)
        )
        
    responsePayload = json.load(response['Payload'])
    print(responsePayload)
    # TODO implement
    return {
        'statusCode': 200,
        'message': 'Success'
    }
