"""def decor(func):
    def innerFunc():
        resul=func()
        return resul*2
    return innerFunc
def num():
    return 5
reus=decor(num)
print(reus())"""


def decor(func):
    def innerFunc():
        resul=func()
        return resul*2
    return innerFunc
@decor
def num():
    return 5

print(num())