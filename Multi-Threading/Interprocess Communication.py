# Program that deals with interprocess communication

# Importing libraries
from threading import *
from time import *

# Data class
class MyData:
    def __init__(self): # Constructor method
        self.data = 0
        self.flag = False # Used to indicate change in data
        self.lock = Lock() # used for simultaneous modifications prevention
        
    def put(self, d): # Put method, writes data
        while self.flag != False:
            pass
        self.lock.acquire()
        self.data = d
        self.flag = True
        self.lock.release()
        
    def get(self): # Get method, reads data
        while self.flag != True:
            pass
        self.lock.acquire()
        x = self.data
        self.flag = False
        self.lock.release()
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

# Creating objects/threads
data = MyData()
t1 = Thread(target=lambda:producer(data))
t2 = Thread(target=lambda:consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()