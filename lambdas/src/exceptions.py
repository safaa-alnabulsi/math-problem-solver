class EmptyInputException(Exception):
    def __init__(self):
        self.message = "The value you entered is empty. The number must be a non negative integer"
        super().__init__(self.message)


class NegativeNumberException(Exception):
    def __init__(self, n):
        self.message = "The value {}' you entered is negative. The number must be a non negative integer".format(n)
        super().__init__(self.message)


class NonDigitNumberException(Exception):
    def __init__(self, n):
        self.message = "The value '{}' you entered is not a digit. The number must be a non negative integer".format(n)
        super().__init__(self.message)
