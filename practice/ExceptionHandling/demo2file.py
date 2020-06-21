try:
    fil=open("demo","w")
    a,b=[int(x) for x in input("Please Enter two Numbers: ").split()]
    c=a/b
    print(c)
    fil.write("writing %d into file" %c)
    
except ZeroDivisionError:
    print("Zero Division Error Please Enter non Zero Divisor")
else:
    print("no exception")
finally:
    fil.close();
    print("File Closed")