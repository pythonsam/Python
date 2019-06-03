# All name variables and methods are public by default in Python

# Protected variable we can define By prefixing the name of your variable with a single underscore, you’re telling others “don’t touch this, unless you’re a subclass”

#  private variable we can define By prefixing the name of your variable with a double underscore,
#  By declaring your data member private you mean, that nobody should be able to access it from outside the class.


class One():
    name = 'public'     # public
    _name = 'protect'   # protect
    __name = 'Pravate'  # pravate

    def _add(self):
        print('Add is: 999 ' ,self.__sub())

    def __sub(self):
        return 'AAAAAA'

ins = One()
ins._add()







