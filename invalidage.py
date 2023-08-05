class InvalidAgeError(Exception):
    pass

def get_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0 or age > 120:
            raise InvalidAgeError("Invalid age. Age must be between 0 and 120.")
        return age
    except ValueError:
        raise InvalidAgeError("Invalid input. Age must be a valid integer.")

if __name__ == "__main__":
    try:
        age = get_age()
        print(f"Your age is {age}.")
    except InvalidAgeError as e:
        print(e)
