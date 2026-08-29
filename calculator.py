#Simple Calculator in python
#it only performs basic operations like addition, subtraction, multiplication and division
def add(a, b):
    """This function takes two numbers as input and returns their sum."""
    return a + b

def subtract(a, b):
    """This function takes two numbers as input and returns their difference."""
    return a - b
def power(a, b):
    """This function takes two numbers as input and returns the first number raised to the power of the second number."""
    return a ** b

def multiply(a, b):
    """This function takes two numbers as input and returns their product."""
    return a * b
def divide(a, b):
    """This function takes two numbers as input and returns their quotient."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b    
def show_operations():
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. exit")

def main():
    while True:
        show_operations()
        choice = input("Select an operation (1/2/3/4/5/6): ")

        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = add(a, b)
            print(f"The result of addition is: {result}")
        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = subtract(a, b)
            print(f"The result of subtraction is: {result}")
        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = multiply(a, b)
            print(f"The result of multiplication is: {result}")
        elif choice == '4':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = divide(a, b)
            print(f"The result of division is: {result}")
        elif choice == '5':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = power(a, b)
            print(f"The result of power is: {result}")
        elif choice == '6':         
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
