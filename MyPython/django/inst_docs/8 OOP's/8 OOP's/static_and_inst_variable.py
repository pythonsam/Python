## Class variable values are same for all instances 
## Instace variable values are different for each instance
class One():
    name = 'sriram'      # class variable or static variable

    def __init__(self, a):
        self.a = a

    def add(self):
        print('inst variable :', self.a,' Static variable :', One.name)

ins = One(33)
ins.add()
inst2 = One(999)
inst2.add()


