import json

print ("hellworld")
def lambda_handler(event, context):
    # TODO implement
    print("event")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
lambda_handler("test", "test")

