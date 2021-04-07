import json
from lambdas.src.exception_handling import validate_input, exception_handler

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def endpoint(event, context):
    try:
        number = validate_input(event, 'n')

        return {
            'statusCode': 200,
            'body': json.dumps(str(fibonacci(number)))
        }

    except Exception as e:

        return exception_handler(e)