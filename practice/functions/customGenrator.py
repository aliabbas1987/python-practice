def customers(x,y):
    while(x<y):
        yield x
        x+=1
result=customers(20, 30)
for i in result:
    print(i)