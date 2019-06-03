## Using super we can call parent class method
class One:
    def add(self):
        print(' One add is ')

    def sub(self):
        print(' One sub is')

class Two():
    def add(self):
        print(' Two add is ')

class Three(Two, One):
    def add(self):
        print(' Three add is')
        #super().add()
        #super(Three, self).add()
        #super(Two, self).__init__()
        ins = One()
        ins.add()

ins = Three()
ins.add()


