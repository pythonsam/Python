
# Lambda functions
# These are anonymous functions means functions without a particular name

# The declaration is assigned to some variable: "some_var" in above
# and this is a function object

some_var = lambda x: x+2

print(some_var(10)) #--> 12
print(some_var(20)) #--> 22

# Pass as many args as needed: 2 here

some_var2 = lambda x,y: x+y

print(some_var2(1,2))
print(some_var2(3,4))


