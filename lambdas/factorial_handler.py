import json
from lambdas.src.exception_handling import validate_input, exception_handler


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def endpoint(event, context):
    try:
        number = validate_input(event, 'n')

        return {
            'statusCode': 200,
            'body': json.dumps(str(factorial(number)))
        }

    except Exception as e:

        return exception_handler(e)
