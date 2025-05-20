class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking loudly!")

# Test

dog1 = Dog("Lucy", "German Shepherd")
dog1.bark()
