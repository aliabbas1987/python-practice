class Student:
    major = 'CSE'
    def __init__(self,rollNumber,name):
        self.rollNumber=rollNumber
        self.name=name
s1=Student(1,'Ali')
s2=Student(2,'zain')
print(s1.major)