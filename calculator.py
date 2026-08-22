def add(a, b):
    """This function takes two numbers as input and returns their sum."""
    return a + b

def subtract(a, b):
    """This function takes two numbers as input and returns their difference."""
    return a - b

def show_operations():
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. exit")

def main():
    while True:
        show_operations()
        choice = input("Select an operation (1/2/3): ")

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
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
