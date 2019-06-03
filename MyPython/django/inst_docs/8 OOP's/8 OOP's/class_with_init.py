class One():
    name = 'sriram'    # Class Variable
    def __init__(self, a, b):
        self.a = a    # Instance variable
        self.b = b

    def add(self):
        print('sum is :' , self.a , self.b, One.name)

    def sub(self):
        print(' sub is : ', self.a - self.b)

    def mul(self):
        print(' mul is :', self.a * self.b)
a = 20
b = 10
ins = One(a, b)
ins.add()
ins1 = One(12, 2)
ins1.add()