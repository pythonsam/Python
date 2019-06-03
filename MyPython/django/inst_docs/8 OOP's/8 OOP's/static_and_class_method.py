# Using @staticmethod decorator we can create static method. For Static method self argument doesn't required.
# Using @classmethod decorator we can create Class method. For class method we have to give cls argument.
class One():
    name = 'sriram'
    @staticmethod
    def add():
        print('add is')

    @classmethod
    def sub(cls):
        cls.name = 'kumar'
        print('class method is', One.name)

inst = One()
inst.add()
inst.sub()
#One.add()
#One.sub()





