minNumber,maxNumber={int(x) for x in input("Enter Minimum and Maximum Number Separated by Comma: ").split(",")}
i=minNumber
if i%2==0:
    i+=1
while(i<=maxNumber):
    print(i)
    i+=2
    