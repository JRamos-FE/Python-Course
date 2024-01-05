# Program dealing with Interprocess Communication using conditions

# Importing libhraries
from threading import *
from time import *

# Data class
class MyData:
    def __init__(self): # Construvtor method
        self.data = 0
        self.cv = Condition()
        
    def put(self, d): # Put method, writes data
        self.cv.acquire()
        self.cv.wait()
        self.data = d
        self.cv.notify()
        self.lock.release()
        sleep(1)
        
    def get(self): # Get method, reads data
        self.cv.acquire()
        self.cv.wait(timeout = 0)
        x = self.data
        self.cv.notify()
        self.cv.release()
        sleep(1)
        return x
    
# Producer function
def producer(data):
    i = 1
    while True:
        data.put(i)
        print('Producer: ', i)
        i += 1
            
# Consumer function
def consumer(data):
    while True:
        x = data.get()
        print('Consumer: ', x)
            
# Creating and calling objects/threads
data = MyData()
t1 = Thread(target=lambda:producer(data))
t2 = Thread(target=lambda:consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()
