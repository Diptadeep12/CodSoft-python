def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")

    operation = input("Enter operation: ")
    
    if operation in ('add', 'subtract', 'multiply', 'divide'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == 'add':
            print(f"Result: {add(num1, num2)}")
        elif operation == 'subtract':
            print(f"Result: {subtract(num1, num2)}")
        elif operation == 'multiply':
            print(f"Result: {multiply(num1, num2)}")
        elif operation == 'divide':
            print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid input. Please enter a valid operation.")

if __name__ == "__main__":
    calculator()
