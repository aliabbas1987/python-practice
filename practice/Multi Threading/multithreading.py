from threading import *
from time import sleep

class MyThread:
    def disNumber(self):
        sleep(1)
        i=0
        while(i<10):
            print(i)
            i=i+1
obj = MyThread()
t = Thread(target=obj.disNumber())
t.start()

t2 = Thread(target=obj.disNumber())
t2.start()

t3 = Thread(target=obj.disNumber())
t3.start()