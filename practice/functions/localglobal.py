x=123

def dis():
    x=786
    print(x)
    print(globals()['x'])
print(x)
z=dis
z()
z()
z()