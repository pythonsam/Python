# lambda function

r = lambda a: a * 2
print(r(2))

nums =[2,6,7]
print(list(filter(lambda n: n % 2 == 0, range(10))))

d = map(lambda n: n ** 2, range(10))
print(d)

r = reduce(lambda x, y: x+y, range(10))
print(r)
print("undo chagnes ")

# Undo all command addded
 # git checkout -- .
 # git checkout -- test.py # for single file
###############################################################
"""
Thirsty branch has been created with the command 
1.git branch thirsty 
2.git checkout thirsty 
"""