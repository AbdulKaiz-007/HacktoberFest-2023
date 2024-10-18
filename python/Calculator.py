def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

def user_choice():
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

                # Get user input for numbers
                try:
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    continue

                # Perform the selected operation
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
