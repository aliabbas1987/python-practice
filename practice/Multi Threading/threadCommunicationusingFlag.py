from threading import *;
from time import *;

class producer:
    def __init__(self):
        self.poducts=[]
        self.c=Condition()
    def produce(self):
        self.c.acquire()
        for i in range(1,5):
            self.poducts.append("product"+str(i))
            sleep(1)
            print("Item Added")
        self.c.notify()
        self.c.release()
class Consumer:
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        self.prod.c.acquire()
        self.prod.c.wait(timeout=0)
        self.prod.c.release()
        print("Order Shipped: ",self.prod.poducts)

p = producer()
c=Consumer(p)

t1=Thread(target=p.produce)
t2=Thread(target=c.consume)

t1.start()
t2.start()