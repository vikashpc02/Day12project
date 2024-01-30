import json
import boto3

lambdaClient = boto3.client('lambda')

def lambda_handler(event, context):
    input = {
        'agentNumber' : 12345,
        'message' : 'A secret message from lambda number 1. Over!!'
    }
    
    response = lambdaClient.invoke(
        FunctionName='ARN',
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
