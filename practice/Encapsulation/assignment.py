class Patient:
    def setID(self,Id):
        self.id=Id
    def getId(self):
        print(self.id)
    def setName(self,Name):
        self.name=Name
    def getName(self):
        print(self.name)
    def setSSN(self,SSN):
        self.ssn=SSN
    def getSSN(self):
        print(self.ssn)
        
pt=Patient()
pt.setID(786)
pt.setName('Ali')
pt.setSSN(1)

pt.getId()
pt.getName()
pt.getSSN()
