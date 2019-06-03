
l1 = (0,2,5,1,3,4)

# Creating iterator using iter keyword
obj = iter(l1)

# Calling next method on the oject. We can do this up to a maximum of length of the list (6 time for above list)
print(next(obj))

print(next(obj))

print(next(obj))

print(next(obj))

print(next(obj))

print(next(obj))

# This will cause an StopIteration error
try:
    print(next(obj))
except StopIteration:
    print("Probably iterator execution finished")

# Regenerate object for futher use
obj = iter(l1)

# Use "for" loop instead of calling next
for i in obj:
    print(i)

# Creating a generator function with yield
def f2(end):
    i=0
    while i < end:
        yield i
        i += 1

# Generator is similar to Iterator
# Calling generator function retruns an object (does not execute the function)
obj = f2(5)

# To start execution we need to call the next method on the object
print(next(obj))

print(next(obj))

print(next(obj))

print(next(obj))

print(next(obj))

# We can call the generator to a maximum of 5 time in above scenario as we initialized it with arg as "5" in f2(5)
try:
    print(next(obj))
except StopIteration:
    print("Error occured; Probably generator execution finished")

# Create another gen object
obj = f2(6)

# Call using "for"
for i in obj:
    print(i)

print("For iteration finished")
# Using iterator/generator in "for" loop never causes error as the execption is internally handled by "for" logic in python

def f3():
    print("Before yield 1")
    yield 1 #pause execution and returns the value 1
    print("Before yield 2")
    yield 2
    print("Before yield 3")
    yield 3
    print("Exiting generator")

obj = f3()

next(obj)
next(obj)
next(obj)

#next(obj) # This line causes error as there are only 3 yields and we finished calling "next" 3 times. Any more calls as this
            # will be invalid and causes StopIteration error

obj = f3()
# Using for loop on generators
for i in obj:
    print(i)