
import time
import threading

class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print("%s started"%(self.name))
        time.sleep(10)
        print("%s exited"%(self.name))

tobj1 = MyThread("Thread1")
tobj2 = MyThread("Thread2")

tobj1.start()
tobj2.start()

tobj1.join()
tobj2.join()

print("Main thread exiting")