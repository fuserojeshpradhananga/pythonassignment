from functools import reduce

def calculate_factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif number == 0 or number == 1:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, number + 1))

print(calculate_factorial(0))1
print(calculate_factorial(1))
print(calculate_factorial(5))
print(calculate_factorial(10))
