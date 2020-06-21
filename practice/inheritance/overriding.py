class BMW:
    def __init__(self,make,model,year):
        self.make=make;
        self.model=model;
        self.year=year;
    def start(self):
        print("Car Started")
    def stop(self):
        print("Car Stopped")
class ThreeSeries(BMW):
    def __init__(self,crouseControlEnabled,make,model,year):
        BMW.__init__(self, make, model, year)
        self.crouseControlEnabled=crouseControlEnabled
class FiveSeries(BMW):
    def __init__(self,ParkingAssistEnabled,make,model,year):
        BMW.__init__(self, make, model, year)
        self.ParkingAssistEnabled=ParkingAssistEnabled
    def start(self):
        print("Button Start")
    def stop(self):
        print("Button Stopped")
        
threeSeries=ThreeSeries(True,"BMW","328i","2020")
fiveSeries=FiveSeries(True,"BMW","528i","2020")
print(threeSeries.crouseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)  
threeSeries.start()
threeSeries.stop() 

print(fiveSeries.ParkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)  
fiveSeries.start()
fiveSeries.stop() 