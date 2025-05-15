class Counter:

    count = 0

    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")

c1 = Counter()
c2 = Counter()

Counter.display_count()
