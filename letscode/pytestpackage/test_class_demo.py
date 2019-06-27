"""
How to use test class to wrap methods under one class
Learn about auto use keywords in fixtures
Assert the result to create a real test scenario
"""


class SomeClassToTests():
    def __init__(self, value):
        self.value = value

    def sumnummbers(self, a, b):
        return a + b + self.value
