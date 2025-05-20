class Employee:
    
    def __init__(self, name):
        self.name = name

class Department:

    def __init__(self, employee):
        self.employee = employee

# Test
emp = Employee("Alice")
dept = Department(emp)
print(f"Employee Name: {dept.emp.name}")
        