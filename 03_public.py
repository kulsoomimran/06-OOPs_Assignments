class Car:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started.")

car_name = Car("Honda")
print(car_name.brand)
car_name.start()
        