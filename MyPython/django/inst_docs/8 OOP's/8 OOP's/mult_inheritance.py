# If you inheritance more than one class that is called multi inheritance
class Mat_Oper():
    name = 'sriram'
    def add(self, a, b):
        print('sum is', a + b)

    def sub(self, a, b):
        print('sub is', a - b)

class Number_Oper():
    def in_ope(self, a, b):
        if a in b : print('exit')

    def not_in_ope(self, a, b):
        if a not in b : print('Not exit')

class Operators(Number_Oper,Mat_Oper):
    def and_oper(self, a, b):
        if a or b: print('and oper')

ins = Operators()
ins.and_oper([],56)
