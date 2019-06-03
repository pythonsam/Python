class One():
    def __init__(self, a,b):
       self.a = a
       self.b = b
       print(' init')

    def add(self):
       print(self.a + self.b)
       
    def sub(self, c):
        print( self.a - self.b - c)

ins = One(50,20)

ins.add()




