def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b
    return x,y,z,u
res=calc(10,5)
print(res)
for i in res:
    print(i)