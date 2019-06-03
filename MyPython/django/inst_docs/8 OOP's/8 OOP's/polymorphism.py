# An object behavior will get change during run time.
# By using inheritence and overloading we can achive it.
class Car:
    def colour(self):
        print('red')

    def music_system(self):
        print('philips')

    def airbags(self):
        print(4)

class Swift(Car):
    def colour(self):
        print('white')

class Varna(Car):
    def colour(self):
        print('block')
    
    def music_system(self):
        print('sony')
    
    def airbags(self):
        print(6)

car_ins = Car()
swift_ins = Swift()
varna_ins = Varna()

car_ins.colour()
swift_ins.colour()
varna_ins.colour()
varna_ins.music_system()













