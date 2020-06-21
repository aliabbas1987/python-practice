from threading import *

def defineNumber():
    i=0
    print(current_thread().getName())
    while(i<10):
        print(i)
        i=i+1
print(current_thread().getName())
t =  Thread(target=defineNumber)
t.start()
