'''
--> For Abstract class we can't create an instance.
--> An abstract method is a method that is declared, but contains no implementation.
--> By defining an abstract base class, you can define a common API for a set of subclasses.
--> By using abc module we can define abstract class.
'''

from abc import ABCMeta,abstractmethod

class One(metaclass=ABCMeta):

    @abstractmethod       # It won't allow to create instance
    def add(self):
        print(' One add ok')

    def sub(self):
        print(' One sub')

a = One()
a.add()

## If you inheritence an abstaruact class you should impliment that all those methods which are abstract ,methods
class Two(One):
    def add(self):
        print(' Two add is')


ins = Two()

