
from functools import reduce # For Reduce function only we need to import 
# Lambda
sum = lambda x,y : x + y
print(sum(4,2))

# filter 
num =[2,4,6,8,9,10,20,24]
even =list(filter(lambda n : n%2 == 0, num))
print(even)

#map 
doubles =list(map(lambda n : n*2 , even))
print(doubles)

#reduce
sum = reduce(lambda a, b : a+ b , doubles)
print(sum)



nums = [3,2,6,8,2,9]
evens  = list(filter(lambda n :  n%2 ==0 ,nums))
print(evens) 
