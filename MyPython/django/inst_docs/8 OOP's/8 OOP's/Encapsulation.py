#Encapsulation is wrapping data and functionality(methods accessing data) together into single uint.

#Giving protection to the class or class members. Using access specifiers/modifiers we can achive it.

class One():
    name = 'public'     # public
    _name = 'protect'   # protect
    __name = 'Pravate'  # pravate

    def __init__(self, a):
        self.a = a

    def add(self):
        print('sum is ')

    def __sub(self):
        print('sub is:')
        cls._add()

ins = One(3)
print('\n ', ins._name)
