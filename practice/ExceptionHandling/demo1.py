try:
    a,b=[int(x) for x in input("Please Enter two Numbers: ").split()]
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Zero Division Error Please Enter non Zero Divisor")