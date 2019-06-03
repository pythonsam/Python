## If you have same method names in class A and class B, then if you Inheritence class A into class B then Class A method will override with class B method.
class A():
    def add(self):
        print('\n A Add is')

class B(A):
    def add3(self):
        print('\n B add is')

class C(B):
    def add2(self):
        print(' \n C add is ')
inst = C()
inst.add()
