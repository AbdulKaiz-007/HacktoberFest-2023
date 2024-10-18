# Contributed by: 
# Name: Abdul Kaiz
# University: KG COLLEGE OF ARTS AND SCIENCE

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    try:
        # Get the temperature in Celsius from the user
        celsius = float(input("Enter the temperature in Celsius: "))
        
        # Convert Celsius to Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)
        
        # Display the result
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Start the program
if __name__ == "__main__":
    main()
