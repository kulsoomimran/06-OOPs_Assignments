class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name # public
        self._salary = salary # protected 
        self.__ssn = ssn # private 

#Test the Employee class
emp = Employee("John Doe", 50000, "123-45-6789")
print(emp.name) # Accessible
print(emp._salary) # Accessible but should be treated as protected
# print(emp.__ssn) # Not accessible, raises an AttributeError
