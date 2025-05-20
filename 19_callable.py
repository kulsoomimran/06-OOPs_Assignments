class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor
    
# Test
m = Multiplier(3)

print(m(10))  

print(callable(m))  # Check if m is callable

print(callable(m(10)))  # Check if the result of m(10) is callable