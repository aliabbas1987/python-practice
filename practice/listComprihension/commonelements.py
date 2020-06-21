a=[1,2,3,4,5]
b=[6,2,8,5,10]
result=[]

'''
Common logic
for i in a:
    if(i in b):
        result.append(i)
print(result)'''

result=[i for i in a if(i in b)]
print(result)