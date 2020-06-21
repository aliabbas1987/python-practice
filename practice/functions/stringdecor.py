def decorfun(func):
    def inner(n):
        resul= func(n)
        resul +="how are you"
        return resul
    return inner
@decorfun    
def hello(name):
    return "hello" + name

print(hello("Ali"))