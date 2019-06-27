class Car(object):
    def __init__(self):
        print ("You Just Created Car Instance")

    def drive(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")


class BMW(Car):
    def __init__(self):
        Car.__init__(self)   # Calling the Car class methods

        print("You Just Created BMW Instance ")


# c = Car()
# c.drive()
# c.stop()

b = BMW()
b.drive()
b.stop()

