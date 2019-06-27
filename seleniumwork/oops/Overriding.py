'''
If you have same method name in Class A and Class B ,then if you inheritence Class A into Class B
then Class A method will Override with Class B Method
'''


class Car(object):
    def __init__(self):
        print('You Just Created the Car Instance')
    def drive(self):
        print('Car Started')
    def stop(self):
        print('Car Stopped')

class BMW(Car):
    def __init__(self):
        Car.__init__(self)
        print('You Just created the BMW Instance')
        super().drive()
    def drive(self):
        print('You are driving BMW')

c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()

