from calculator import add, subtract, multiply, divide

def main():
    """Gets user input, performs calculation, and prints the result."""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator. Please use +, -, *, or /.")
            return

        print(f"The result is: {result}")

    except ValueError:
        print("Invalid input. Please enter numbers only for the first and second number.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
