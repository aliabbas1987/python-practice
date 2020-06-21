class noOFObject:
    numberofObject=0
    def __init__(self):
        noOFObject.numberofObject+=1
    @staticmethod
    def displayCount():
        print(noOFObject.numberofObject)
o1=noOFObject()
o2=noOFObject()
noOFObject.displayCount()