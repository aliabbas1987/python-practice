import os,sys
from _tkinter import create

if os.path.exists("test.txt"):
    f=open("text.txt",'a')
else:
    create("test.txt")
    f=open("text.txt",'a')
    
s=""
print("Enter values in file, when you want to terminate press #")
while s != '#':
    s=input()
    f.write(s)
f.write("#")
f.close()

