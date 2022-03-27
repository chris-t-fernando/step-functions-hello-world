import json

# import requests
# step-functions-hello-world


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": event["name"],
            }
        ),
    }
