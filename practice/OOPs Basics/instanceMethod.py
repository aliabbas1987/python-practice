class Product:
    def __init__(self):
        self.name='Iphone'
        self.description='High Price'
        self.price = 1000
    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)
pl=Product()
pl.display()
