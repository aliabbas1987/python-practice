lst=[10,20,"ali",5,-5,6]
print(lst)
print(lst[3])
print(lst[3:4])
print(lst*3)
print(len(lst))
lst.append(30)
lst.remove("ali")
del(lst[0])
print(lst)
#lst.clear()
#print(lst)
#print(max(lst))
#print(min(lst))
lst.insert(3, 99)
#print(lst)
lst.sort(reverse=True)
print(lst)