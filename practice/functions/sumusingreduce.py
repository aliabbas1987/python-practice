from functools import reduce
lst =[5,2,3,4,20]
resl=reduce(lambda x,y:x+y, lst)
print(resl)
