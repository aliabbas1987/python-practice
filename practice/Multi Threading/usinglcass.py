from threading import *

class MyThread:
    def disNumber(self):
        i=0
        while(i<10):
            print(i)
            i=i+1
obj = MyThread()
t = Thread(target=obj.disNumber())
t.start()