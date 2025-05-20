def add_greeting(cls):
    def greet(self):
        return "Hello from the Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test
p = Person("Alice")
print(p.greet())  