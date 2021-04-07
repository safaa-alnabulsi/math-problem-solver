import json
from lambdas.src.exceptions import NegativeNumberException, NonDigitNumberException, EmptyInputException


def validate_input(event, key):
    try:
        event_body = json.loads(event['body'])
        n = event_body[key]
    except KeyError as e:
        raise EmptyInputException()

    if n == "":
        raise EmptyInputException()
    elif not n.lstrip('-').isdigit():  # the minus in negative numbers is not considered a digit
        raise NonDigitNumberException(n)
    elif int(n) < 0:
        raise NegativeNumberException(n)

    return int(n)


def exception_handler(e):
    return {
        'statusCode': 400,
        'body': json.dumps(str(e))
    }
