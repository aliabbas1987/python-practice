import re
str="take up One idea at time, One great idea"
reustl = re.search(r'o\w',str)
print(reustl)

reustl = re.findall(r'o\w\w',str)
print(reustl)

reustl = re.match(r't\w\w',str)
print(reustl)