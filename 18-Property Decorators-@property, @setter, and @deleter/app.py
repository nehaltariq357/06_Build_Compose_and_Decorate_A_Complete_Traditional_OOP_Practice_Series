# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self,price):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value >=0:
            self._price = value
        else:
            print("price cannot be negative")

    @price.deleter
    def price(self):
        del self._price



p1 = Product(100)
print(p1.price) # 100 , calls the @property

p1.price = 200
print(p1.price) # 200 , calls the @price.setter


del p1.price # calls the @price.deleter

try:
    print(p1.price)
except AttributeError:
    print("price is deleted")