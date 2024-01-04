# Progrma that deals with interprocess communication

# Importing libraries
from threading import *
from time import *

# Data class
class MyData:
    def __init__(self):
        self.data = 0
        self.flag = False
        self.lock = Lock()
        
    def put(self, d):
        while self.flag != False:
            pass
        self.lock.acquire()
        self.data = self.flag = True
        self.lock.relaese()
        
    def get(self):
        while self.flag != True:
            pass
        self.lock.acquire()
        x = self.acquire()
        