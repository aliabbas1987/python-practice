class Course:
    def __init__(self,name,ratingList):
        self.name=name
        self.ratings=ratingList
    def avg(self):
        NumberOfRatings= len(self.ratings)
        avge=self.ratings/NumberOfRatings
        print("Avarage rating for ", self.name, " is ",avge)
pC=Course('python',[1,2,3,4,5])

print(pC.name)
print(pC.ratings)
pC.avg()
pC1=Course('C#',[5,5,5,5,5])

print(pC1.name)
print(pC1.ratings)
pC1.avg()
