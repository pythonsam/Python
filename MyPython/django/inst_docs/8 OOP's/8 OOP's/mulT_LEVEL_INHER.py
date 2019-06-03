# We can inherit a derived class from another derived class, this process is known as multilevel inheritance
# In multilevel inheritance, we inherit the classes at multiple separate levels. 
# We have three classes A, B and C, where A is the super class, B is its sub(child) class and C is the sub class of B.

class Mat_Oper():
    name = 'sriram'
    def add(self, a, b):
        print('sum is', a + b)

    def sub(self, a, b):
        print('sub is', a - b)

class Number_Oper(Mat_Oper):
    def in_ope(self, a, b):
        if a in b : print('exit')

    def not_in_ope(self, a, b):
        if a not in b : print('Not exit')

class Operators(Number_Oper):
    def and_oper(self, a, b):
        if a or b: print('and oper')
ins = Operators()
ins.and_oper([],56)
