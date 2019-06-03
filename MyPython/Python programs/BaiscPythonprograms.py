#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sureshkumarkadi
#
# Created:     17-08-2018
# Copyright:   (c) sureshkumarkadi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
###print numbers from 0 t0 14
##x = 1
##
##for x in range(0,15):
##    x  = x*1
##    print x
##
###print even numbers between 0 t0 14
##x = 2
##
##for x in range(0,15):
##    x  = x*1
##    print x
##
### seperate even and odd numbers from a list
##l = [0,1,2,3,4,5,6,7,8,9,10]
##
##even = []
##odd = []
##
##for g in l:
##    if (g%2==0):
##        even.append(g)
##    else:
##        odd.append(g)
##print even
##print odd
##
### split path
##import os
##
##path  = os.path.splitext('E:\RegistrationFormautomation\Data\Testdata.json')
##
##print path[0]
##print path[1]
##
###split words
##
##string = 'suresh % kumar & kadi *'
##
##name = string.split(" ")
##
##print name
##
##print name[0]+name[2]
##
###how to swap two numbers
##
##x =1
##y = 2
##
##x,y  = y,x
##
##print x
##print y
##
### how to swap dictionary values
##
##dict1 = {"x1":1,"y1":2,"z1":3}
##
##print {val:key for (key,val) in dict1.iteritems()}
##
##double = lambda x: x * 2
###double = double+1
##print(double(1))
##
###print numbers in a list
###print(list(range(1,101)))
##
###print numbers from 0 to 100 using if condition
##
##def print100numbers(n):
##    if n > 0:
##        print100numbers(n-1)
##        print n
##
##print100numbers(100)

#print fibnocci series

##def fib():
##    a,b = 1,1
##    while True:
##        yield a
##        a,b  = b,a+b
##        print a
##        print b
##n=0
##for i in fib():
##    if n >= 5:
##        break;
##    print i
##    n += 1

##def my_gen():
##    a = 1
##    while True:
##    #print('This is printed first')
##    # Generator function contains yield statements
##        yield a
##        a = a+1
##    #print n
##
### Using for loop
##n = 1
##for item in my_gen():
##    if n>=3:
##        break;
##    print(item)
##    n+= 1

##def no(n):
##    if n>=0:
##        no(n-1)
##        print n
##no(100)

a = xrange(1,5)

#for a1 in a:
    #print list(a1)

a2 = range(1,10)
print "list is :",list(a2)
print tuple(a2)

#mylist = [1, 2, 3]
##mylist = (x*x for x in range(3))
## for i mylist:
##     print i
##import requests
##from selenium import webdriver
##
##browser =webdriver.Chrome("C:\Users\sureshkumarkadi\Downloads\chromedriver_win32\chromedriver.exe")
##
##browser.get('https://google.co.in')
##
##links = browser.find_elements_by_tag_name("a")
##
##for link in links:
##    urls = requests.head(link.get_attribute('href'))
##    print link.get_attribute('href'),urls.status_code

#random number generation
import random

print random.randrange(0,10)

s = 'catandapple'

print s[6:]
print s[:6]
print s[0]

#Basic Syntax:

#result = [expression iteration filter]

#print numbers from 0 to 7
x= [i for i in range(8)]
print x

#print only even numbers using list comprehension
x = [i for i in range(100) if i%2==0]
print x

#create a list of squares
x = [i**2 for i in range(8)]
print x

#create a list of squares usng normal methods
s  = []

for x in range(10):
    s.append(x**2)
print s

#adding two numbers using normal function
def numners(x,y):
    return x+y
print numners(1,2)

#adding two numbers using lampda function
add = lambda x,y:x+y
print add(1,2)
#or
print (lambda x,y:x+y)(1,2)

#Square of a each number using lambda

list1  = [1,2,3,4,5,6,7,8]

squarenumbers= map(lambda x:x**2,list1)
print squarenumbers

#evennumbers using lampda function

list1  = [1,2,3,4,5,6,7,8]

evennumbers= filter(lambda x:x%2==0,list1)
print evennumbers

#how to use lambda function inside a function

def doubles(n):
    return lambda a:a*n

doubler = doubles(2)
print doubler(11)

import time

def timecalculation(func):
    def wrapper():
        starttime = time.time()
        func()
        endtime = time.time()
        print endtime-starttime
    return wrapper


squares = []
@timecalculation
def calcsuare():
    for x in range(10):
        squares.append(x**2)

cubes = []
@timecalculation
def calccube():
    for x in range(100):
        cubes.append(x*x*x)

calcsuare()
calccube()

class Student(object):
    """
    Returns a ```Student``` object with the given name, branch and year.

    """
    def __init__(self, name, branch, year):
            self.name = name
            self.branch = branch
            self.year = year
            print("A student object is created.")
            print self.name
            print self.branch
            print self.year

    def print_details(self):
        """
        Prints the details of the student.
        """
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)

std1 = Student('suresh','ece',2018)
#std1 = Student()
#std1.print_details()

#download a file from web

##import requests
##file_url = "http://python.org/python_image.png"
##
##image  = requests.get(file_url)
##
##with open('E:\eTender\logo.png','w+') as f:
##    f.write(image.content)

import copy

list1 = [[1,2,3],[4,5,6]]
#shallow copy - Shallow copy creates a copy of the object but references each element of the object
newlist = copy.copy(list1)

newlist[0][1]=10

print list1
print newlist

list1 = [[1,2,3],[4,5,6]]
#deep copy - Deep copy creates a copy of the object and elements of the object
newlist = copy.deepcopy(list1)

newlist[0][1]=10

print list1
print newlist

#Get all keys from a Dictionary

json  = {'x':1,'y':2,'z':3}

print json.keys()

#Get all values from a Dictionary

json  = {'x':1,'y':2,'z':3}

print json.values()

#create a dictionary using tuples in python

tuple  = (1,2),(2,3)

print dict(tuple)

#create a dictionary using List in python

List  = [1,2],[2,3]

print dict(List)

#convert a string to all lowercase?

string = 'suresh'

print string.lower()

print string.upper()

# change case for all letters in string
string = 'SURESH'

print string.swapcase()
#The following code gives all lower or upper case letters in a document
with open('E:/test.txt','r') as fh:
    count = 0
    text = fh.read()
    for character in text:
        if character.islower():
            print character,
            count += 1
#Sorting a list first method:
list1 = [1,0,2,2,0,5,6,3,0,3,0]

list2 = [i for i in list1]

list2.sort()

print (list2)

#Sorting a list second method:
list1 = [1,0,2,2,0,5,6,3,0,3,0]

list1.sort()

print (list1)

#how to reverse a list

print list(reversed(list1))

# lambda function for filter,map and reduce
list1  = [1,2,4,5,6,7,8,9,10]

print filter(lambda x:x%2==0,list1)
print map(lambda x:x*2,list1)
print reduce((lambda x,y:x+y),list1)

#conver number to list

num = 23332432432
#using map function
print map(int,str(num))

#ising list comprehension
print [int(x) for x in str(num)]

#findout last two greater number from a list
newlist =  filter(lambda x:x>8,range(10))

print newlist

#Calculating sum of a list numbers

num_List1 = [1,2,3,4,5,6]

def listsum(num_List1):
    listsum = 0
    for i in num_List1:
        listsum = listsum + i
    return listsum

print listsum(num_List1)

print sum(x for x in num_List1)

import random
#read random lines from a file
def random_lines(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print random_lines('E:/test.txt')

#Count no.of lines in a docunemt

print sum(1 for line in open('E:/test.txt'))

# how to achive multithreading

import time
import threading

def anotherfuncton(function):

    ''' this is to explain about decorator
    second line
    third line
    '''
    def wrapper():
        starttime = time.time()
        function()
        endtime  = time.time()
        print endtime-starttime

    return wrapper

square  =[]
@anotherfuncton
def squares():
    for i in range(10):
        square.append(i**2)
        #time.sleep(1)
    print square,

cube=[]
@anotherfuncton
def cubes():
    for i in range(10):
        cube.append(i*i*i)
        #time.sleep(1)
    print cube,

##squares()
##cubes()

t1 = threading.Thread(target=squares)
t2 = threading.Thread(target=cubes)

t1.start()
t2.start()

t1.join()
t2.join()

#Single inheritance in python
class A1():
    def a(self):
        return 2

class B1(A1):
    def b(self):
        return 3

obj = B1()
print obj.a()
#Inheritance in python
class student():
    def __init__(self,name,year,branch):
        self.name = name
        self.year = year
        self.branch = branch

    def get_stdentdetials(self):
        print("name:" ,self.name)
        print("Year:" ,self.year)
        print("branch:" ,self.branch)

class subject0(student):
    def __init__(self,name,year,branch,sub1,sub2,sub3):
        student.__init__(self,name,year,branch)
        self.sub1 = sub1
        self.sub2  = sub2
        self.sub3 = sub3

    def get_stdentdetials(self):
        student.get_stdentdetials(self)
        print("subject1:" ,self.sub1)
        print("subject2:" ,self.sub2)
        print("subject3:" ,self.sub3)

s1 = subject0('suresh',2018,'ece','eng','sci','maths')
s1.get_stdentdetials()

#Collections - OrderedDict

'''This module implements specialized container datatypes providing
alternatives to Python's general purpose built-in containers, dict,
list, set, and tuple.

* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing values.'''

from collections import OrderedDict
orderdict1 = OrderedDict()

dict1 = {'Age':18,'name':'suresh','place':'Amalapuram'}
dict2 = {'name':'suresh','Age':18,'place':'Amalapuram'}

for k,v in dict1.items():
    print k,v

print dict1==dict2
orderdict1['name'] = 'suresh'
orderdict1['Age'] = 18
orderdict1['place'] = 'Amalapuram'

orderdict2 = OrderedDict()
orderdict2['Age'] = 18
orderdict2['name'] = 'suresh'
orderdict2['place'] = 'Amalapuram'

for k,v in orderdict1.items():
    print k,v

print orderdict1 == orderdict2

print dict1.keys()
print dict1.values()

print orderdict1.keys()
print orderdict1.values()

#Collections - deque
from collections import deque

d = deque()

d.append(2)
d.append(1)
d.append(3)

print d
print d.count(2)

d.appendleft(4)
d.appendleft(5)
d.appendleft(6)

print d
print d.count(4)

d.extend('abc')
print d
d.append('abc')
print d
d.extend((1,2,3))
print d
d.append((123))
print d
d.extendleft('xyz')
print d
#d.clear()
#print d
d.pop()
print d
d.popleft()
print d
print d.count(1)
d.remove(1)
print d
d.reverse()
print d
#Collections - Counter
from collections import Counter

#list = [1,2,3,4,5,6,7,1]
#print len(list)

d= Counter('Amalapuram')
print d

print list(d.elements())
print d.most_common(3)

from collections import defaultdict

d=defaultdict(lambda: 6.6)
d['name']='suresh'
d['Age']=18

print d['name']
print d['Age']

print d['height']
print d['Sex']

#reverse a string

def reverse1(s):
  str = ""
  for i in s:
    str = i + str
  print str

reverse1('sursh')

#Sets in python

newset = set(['Telugu','English','Maths'])
newset.add('Sci')
newset.discard('Telugu')
print newset

#Encapsulation in Pyhotn

class A:
    def __init__(self):
        self.__name='suresh'
        self.__age=31

    def drive(self):
        print("name:",self.__name)
        print("age:",self.__age)

    def setage(self,age1):
        self.__age=age1
        print("age:",self.__age)
obj=A()
obj.drive()
obj.__age=40
obj.drive()

#Maximum two numbers from a list
import heapq

print heapq.nlargest(2,list1)











