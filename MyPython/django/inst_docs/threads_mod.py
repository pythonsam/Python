import time
import threading

def f1(a,b):
    print("f1 started")
    print(a,b)
    time.sleep(10)
    print("f1 exited")

def f2():
    print("f2 started")
    time.sleep(5)
    print("f2 exited")

t1 = time.time()
# f1()
# f2()
# t2 = time.time()
tobj1 = threading.Thread(target=f1, args=(10,20))
tobj2 = threading.Thread(target=f2)

tobj1.start()
tobj2.start()

tobj1.join()
tobj2.join()

print("Main thread exited")
t2 = time.time()
print("Time taken is %s"%(t2-t1))
    
