from abc import abstractmethod,ABC

class BMW(ABC):
    def __init__(self,make,model,year):
        self.make=make;
        self.model=model;
        self.year=year;
    def start(self):
        print("Car Started")
    def stop(self):
        print("Car Stopped")
    @abstractmethod
    def drive(self):
        pass
class ThreeSeries(BMW):
    def __init__(self,crouseControlEnabled,make,model,year):
        BMW.__init__(self, make, model, year)
        self.crouseControlEnabled=crouseControlEnabled
    
    def drive(self):
        print("Three Series")
class FiveSeries(BMW):
    def __init__(self,ParkingAssistEnabled,make,model,year):
        BMW.__init__(self, make, model, year)
        self.ParkingAssistEnabled=ParkingAssistEnabled
    def drive(self):
        print("Three Series")
threeSeries=ThreeSeries(True,"BMW","328i","2020")
print(threeSeries.crouseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)  
threeSeries.start()
threeSeries.stop() 