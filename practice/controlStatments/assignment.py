marksList=[int(x) for x in input("Enter Marks of three Subjects seprated by comma = ").split(",",3)]
    
if(marksList[0]< 35 or marksList[1]< 35 or marksList[2]< 35):
    print("You have failed the exam, Please try again")
elif(marksList[0]>= 35 or marksList[1]>= 35 or marksList[2]>= 35):
    avarage= (marksList[0]+marksList[1]+marksList[2])/3
    if(avarage<=59):
        print("You have C Grade")
    elif(avarage<=69):
        print("You have B Grade")
    else:
        print("You have A Grade")
else:
    print("Please Input subject and Marks one by one, Maths, Physicss, Chemistrys")