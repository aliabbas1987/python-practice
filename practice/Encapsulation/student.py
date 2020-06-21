
class Student:
    def __init__(self):
        self.__id=123
        self.__name='Ali'
    def display(self):
        print(self.__id)
        print(self.__name)
s=Student()
s.display()

#can't display directly private variables but can access using name mangling

print(s._Student__id)