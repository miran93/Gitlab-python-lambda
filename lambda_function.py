import json


def lambda_handler(event, context):
    message = "Hi Miran"
    with open("some_file.txt") as f:
        message += f.read()
    f.close()

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
