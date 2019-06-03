
# Some class inheriting an inbuilt eception type class
class CustomException(Exception):
    def __init__(self, value):
        print(value)
        self.add_logic()

    def add_logic(self):
        print("additional logic being executed")

# Raising the user defined exception
# raise CustomException("My custom exception")


class NoSuchFileException(IOError):
    def __init__(self, value):
        print("No such file available: %s"%value)


try:
    fobj=open("SomeUnknownFile.txt")
except Exception as e:
    raise NoSuchFileException("File not found. %s"%e)

