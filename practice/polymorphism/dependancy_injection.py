class Flight:
    def __init__(self,engine):
        self.engine=engine
        
    def startEngine(self):
        self.engine.start();
class AirBusEngine:
    def start(self):
        print("Engine Start")
class BoingEngine:
    def start(self):
        print("Engine Start")

ae=AirBusEngine()
f=Flight(ae)
f.startEngine()

be=BoingEngine()
f=Flight(be)
f.startEngine()