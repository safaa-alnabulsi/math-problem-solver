import json
from lambdas.src.exception_handling import validate_input, exception_handler

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def endpoint(event, context):
    try:
        n = validate_input(event, 'n')
        m = validate_input(event, 'm')

        return {
            'statusCode': 200,
            'body': json.dumps(str(ackermann(m, n)))
        }

    except Exception as e:

        return exception_handler(e)
