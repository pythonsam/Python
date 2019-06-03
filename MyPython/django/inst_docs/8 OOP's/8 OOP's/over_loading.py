'''
1. If we have different methods with same name in a class with different arguments that is called Method over loading.
2. Python doesn't support for method over loading.
'''

class A():
    def add(self):
        print(' 1 Add is')
        
    def add(self, a):
        print(' 2 A Add is', a + 10)

    def add(self, a, b):
        print(' 3 A Add is', a + b)

    def add(self, a, b, c):
        print(' 4 A Add is', a + b + c)


inst = A()
inst.add()
