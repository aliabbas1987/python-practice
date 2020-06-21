class Student:
    def setID(self,Id):
        self.Id=Id
    def getID(self):
        return self.Id
    def setName(self,Name):
        self.Name=Name
    def getName(self):
        return self.Name
s=Student()
s.setID(123)
s.setName('Ali')
print(s.getID())
print(s.getName())