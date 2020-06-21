from threading import *

def EvenNumbers():

    i=1
    while (i<=100):
            if(i%2==0):
                print(i)
                i+=1


def OddNumbers():

    i=1
    while (i<=100):
        if(i%2!=0):
             print(i)
             i+=1

def MainThread():

    i=1

    while (i<=100):

        print(i)

        i+=1



t1= Thread(target=EvenNumbers)

t1.start()

t2= Thread(target=OddNumbers)

t2.start()

t3= Thread(target=MainThread)

t3.start()