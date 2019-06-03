# Lambda function 
# It's an anonymous function one time use only 
# n num of arguments but only one expression 

f = lambda a : a *5
result = f(5)
print(result)


add = lambda a, b : a + b
result_add = add(2,3)
print(result_add)

# Filter - Using lambda function filter is used to filter some values based on logic
# It return value is True then only it stores 

# to Print even nums 

nums =[1,2,3,3,4,4]

even = list(filter(lambda n : n %2 == 0, nums))
print(even)

# Map is function it takes 2 argumetns 
# Map applies a function to every element in an iterable 
# map() returns a iterator 

doubles = list(map(lambda n :n *2 ,even))
print(doubles)

from functools import reduce
# reduce is used to reduce a sequance pair wise until we reach a single value 
sum = reduce(lambda a, b : a + b ,doubles)
print(sum)

print('###########################################################')

r =list(filter(lambda n : n %2 == 0 ,range(10)))
print(r)

d = list(map(lambda n : n *2 ,range(10)))
print(d)

sum = reduce(lambda a, b : a + b ,range(10))
print(sum)
print('###########################################################')

# zip - it is used to map the similar index of mutiple containers so that they can be used as single entity 

# syntax : zip(*iterator)
# Returns the single iterator object having mapped values from all the containers
name =['roger','nick']
rno=[1,2]
mapped = zip(name, rno)
print(mapped)
m = set(mapped)
print(m)

# to Unzip the mapped items 
name = zip(*mapped)
print(name)

rno = zip(*mapped)
print(rno)

print('***********************************')
range(10)


