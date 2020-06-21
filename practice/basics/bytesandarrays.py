lst=[10,20,30,40]
b=bytes(lst)
print(type(b))

b=bytearray(lst)
print(type(b))
b[2]=33
print(b[2])