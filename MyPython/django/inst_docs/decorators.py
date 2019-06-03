
import time

#This is a decorator function
#Takes function object as argument and returns
#another function object as argument
def time_calc(fobj):
    def wrapper(*args, **kwargs):
        st = time.time()
        fobj(*args, **kwargs)
        et = time.time()
        print("Time taken is %s secs"%(et-st))
    return wrapper  #Returning a function object

@time_calc   #Decorator applied with "@" syntax
def f1(a):
    print("In f1: %s"%a)
    time.sleep(2)

@time_calc  
def f2():
    print("In f2")
    time.sleep(3)

@time_calc
def f3(a,b):
    print("In f3: %s, %s"%(a,b))
    time.sleep(5)

f1(1)  #Calling this way will actually be called as "time_calc(f1)(1)"
       #internally by python while program is being executed

f2()   # This will be time_calc(f2)()
f3(5,10)  #This will be time_calc(f3)(5,10)