class One():
	def __init__(self, a , b):
		print('__init__')
		self.a = a
		self.b = b
	def adding(self):
		print("add is :", self.a + self.b)
	def sub(self):
		print("sub is :", self.a - self.b)
a = 20
b = 30		
	
inst = One(a,b)
inst.adding()
inst.sub()	