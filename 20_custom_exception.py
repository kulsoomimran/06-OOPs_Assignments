class InvalidAgeError():
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")

try:
    check_age(16)
except InvalidAgeError as e:
    print(f"Invalid age: {e}")