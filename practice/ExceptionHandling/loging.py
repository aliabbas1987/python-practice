
import logging
logging.basicConfig(filename="demo.log",level=logging.DEBUG)
try:
    fil=open("demo","w")
    a,b=[int(x) for x in input("Please Enter two Numbers: ").split()]
    c=a/b
    print(c)
    fil.write("writing %d into file" %c)
    logging.info("record %d saved in" %c)
except ZeroDivisionError:
    print("Zero Division Error Please Enter non Zero Divisor")
    logging.error("Divided by Zero")
else:
    print("no exception")
finally:
    fil.close();
    print("File Closed")