class programmer:
    def setName(self,m):
        self.name=m
    def getName(self):
        return self.name
    def setSalary(self,m):
        self.salary=m
    def getSalary(self):
        return self.salary
    def setTechnology(self,m):
        self.technology=m
    def getTechnology(self):
        return self.technology

pr=programmer()
pr.setName('Ali')
pr.setSalary('225,000')
pr.setTechnology('Cold Fusion, PhP, Asp.net')

print(pr.getName())
print(pr.getSalary())
print(pr.getTechnology())