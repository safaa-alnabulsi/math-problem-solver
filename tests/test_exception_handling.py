import unittest
import json
from lambdas.src.exception_handling import validate_input, exception_handler
from lambdas.src.exceptions import NegativeNumberException, NonDigitNumberException, EmptyInputException


class TestExceptionHandling(unittest.TestCase):

    def test_n_is_empty(self):
        event_input = {"body": ""}
        with self.assertRaises(EmptyInputException):
            _ = validate_input(event_input, 'n')

    def test_n_is_empty(self):
        event_input = {"body": json.dumps({"n": ""})}
        with self.assertRaises(EmptyInputException):
            _ = validate_input(event_input, 'n')

    def test_n_is_non_digit(self):
        event_input = {"body": json.dumps({"n": "a"})}
        with self.assertRaises(NonDigitNumberException):
            _ = validate_input(event_input, 'n')

    def test_n_is_negative(self):
        event_input = {"body": json.dumps({"n": "-5"})}
        with self.assertRaises(NegativeNumberException):
            _ = validate_input(event_input, 'n')

    def test_n_valid(self):
        event_input = {"body": json.dumps({"n": "4"})}
        self.assertEqual(validate_input(event_input, 'n'), 4)

    def test_exception_handler(self):
        e = Exception('something went wrong')
        expected_output = {
            'statusCode': 400,
            'body': json.dumps(str(e))
        }
        self.assertEqual(exception_handler(e), expected_output)


if __name__ == '__main__':
    unittest.main()
