class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getting price...")
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        print("Setting price...")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Test

p = Product(100)

print(p.price)  # Getting price...

p.price = 150  # Setting price...

print(p.price)  # Getting price...

del p.price  # Deleting price...

# print(p.price)  # This will raise an AttributeError since price has been deleted