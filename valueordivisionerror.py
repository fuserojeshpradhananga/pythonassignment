def perform_division(num1, num2):
    try:
        result = num1 / num2
        return result
    except ValueError:
        raise ValueError("Error: Please enter valid integers.")
    except ZeroDivisionError:
        raise ValueError("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        result = perform_division(num1, num2)
        print(f"The result of {num1} / {num2} is {result:.2f}")
    except ValueError as e:
        print(e)
