from threading import *

class BookMyBus:
    def __init__(self,availableSeats):
        self.availableSeats = availableSeats
        self.l=Semaphore()
    def buy(self, seatRequested):
        self.l.acquire()
        if(self.availableSeats>=seatRequested):
            print("Total Seats Available: ",self.availableSeats)
            print("Confirm Seat")
            print("Processing Seat")
            print("Print Ticket")
            self.availableSeats-=seatRequested
            self.l.release()
        else:
            print("Seat not available")

obj = BookMyBus(10)

t1 = Thread(target=obj.buy,args=(3,))
t2 = Thread(target=obj.buy,args=(4,))
t3 = Thread(target=obj.buy,args=(4,))


t1.start()
t2.start()
t3.start()