from abc import abstractmethod,ABC
class TouchScreenLaptops(ABC):
    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass
class HP(TouchScreenLaptops):
    
    def scroll(self):
        print("mouse Scrolled hp")
    @abstractmethod
    def click(self):
        TouchScreenLaptops.click(self)
class Dell(TouchScreenLaptops):
    
    def scroll(self):
        print("mouse Scrolled dell")
    @abstractmethod
    def click(self):
        TouchScreenLaptops.click(self)
class HPNotebook(HP):
    
    def click(self):
        print("HP mouse clicked")
   
class DellNotebook(Dell):
    
    def click(self):
        print("Dell mouse clicked")
d=DellNotebook()
h=HPNotebook()
d.click()
d.scroll()
h.click()
h.scroll()


    