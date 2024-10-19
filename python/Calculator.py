def add(a, b):
    """Return the sum of a and b."""
    return int(a + b)

def sub(a, b):
    """Return the difference of a and b."""
    return int(a - b)

def mul(a, b):
    """Return the product of a and b."""
    return int(a * b)

def div(a, b):
    """Return the quotient of a and b, handling division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return int(a / b)

def get_number(prompt):
    """Get a valid integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def user_choice():
    """Display the calculator menu and process user choices."""
    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        user_input = input("Enter your choice (1-5): ")

        if user_input.isdigit():
            user_input = int(user_input)

            if 1 <= user_input <= 5:
                if user_input == 5:
                    print("Exiting the calculator. Goodbye!")
                    break

                a = get_number("Enter the first number: ")
                b = get_number("Enter the second number: ")

                if user_input == 1:
                    result = add(a, b)
                elif user_input == 2:
                    result = sub(a, b)
                elif user_input == 3:
                    result = mul(a, b)
                elif user_input == 4:
                    result = div(a, b)

                print("Result:", result)
            else:
                print("Please enter a number between 1 and 5.")
        else:
            print("Please enter a valid number.")

# Start the calculator
user_choice()
