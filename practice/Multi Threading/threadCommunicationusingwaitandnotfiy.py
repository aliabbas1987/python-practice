from threading import *;
from time import *;

class producer:
    def __init__(self):
        self.poducts=[]
        self.orderPlace=False
    def produce(self):
        for i in range(1,5):
            self.poducts.append("product"+str(i))
            sleep(1)
            print("Item Added")
        self.orderPlace=True
class Consumer:
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        while self.prod.orderPlace==False:
            sleep(0.2)
        print("Order Shipped: ",self.prod.poducts)

p = producer()
c=Consumer(p)

t1=Thread(target=p.produce)
t2=Thread(target=c.consume)

t1.start()
t2.start()