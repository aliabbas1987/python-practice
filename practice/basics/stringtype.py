from _ast import Is
s=' you are great '
print(s)
ms="""
your name Is
ali abbas
you are great person
"""
#print(ms*2)
#print(len(ms))
#print(ms[0:8])
#print(ms[-3:-1])
#print(ms[0:9:2])
print(s.strip(s))
print(s.lstrip(s))
print(s.rstrip(s))
print(ms.find("bb",0,30))
print(ms.count("b"))
print(ms.replace("great", "supper"))
print(ms.upper())
print(ms.lower())
print(ms.title())