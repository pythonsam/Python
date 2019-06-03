# This import is not needed if executing with python version 2
from functools import reduce


def f1(a):
    return a*a

# Without map
l = []
for i in range(10,20):
    l.append(f1(i))

#With map
#Appends the return value from function object "f1" for each value from the range
l1 =  list(map(f1, range(10, 20)))
print(l1)

def f2(a):
    if a%2 == 0: #Means an even no.
        return True

#Appends the value to "l2" for which the function object "f2" returns True for each value from range
l2 = list(filter(f2, range(10, 20)))

print(l2)

# Reduce
def sum(a,b):
    return a+b

#For 1st iteration takes the args a,b values from range,
#then from on 1st arg is return val of func object "sum" and 2nd arg is from the range
val = reduce(sum, range(10))
print(val)


