import re
stri="take up One 01-01-2020 idea at time, 12-11-2020 One great idea"
resu=re.findall(r'O\w+',stri)
print(resu)

resu=re.findall(r'\d{1,2}-\d{1,2}-\d{1,4}',stri)
print(resu)