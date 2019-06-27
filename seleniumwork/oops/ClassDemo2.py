"""
Class - Class is a Blueprint of an Object
"""


class Car(object):
    wheels = 4  # Member Variable

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the Car:", self.make)
        print("Model of the Car:", self.model)


print(Car.wheels)
c1 = Car('BMW', 'E350')
c1.info()
c1.wheels = 1  # Instance Variable
print(c1.wheels)
c2 = Car("Benz", 'C750')
c2.info()
print(Car.wheels)