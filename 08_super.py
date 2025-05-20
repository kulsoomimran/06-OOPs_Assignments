class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Test
teacher = Teacher("Alice", "Math")
print(f"My {teacher.subject} teacher is {teacher.name}.")  