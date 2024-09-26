# Function to perform the chosen operation
def perform_operation(choice, num1, num2):
    if choice == 'A':
        return num1 * num2
    elif choice == 'B':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    elif choice == 'C':
        return num1 + num2
    elif choice == 'D':
        return num1 - num2
    elif choice == 'E':
        # Check for division by zero in remainder operation
        if num2 == 0:
            return "Error: Division by zero"
        return num1 % num2
    else:
        return "You did not enter a valid choice"

# Display menu options
print("Select one of the following options: ")
print("Enter A for Multiply: ")
print("Enter B for Divide: ")
print("Enter C for Add: ")
print("Enter D for Subtract: ")
print("Enter E for Remainder Division: ")

# Get user's choice
choice = input("Enter your choice: ").upper()

# Prompt the user to enter two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Perform the chosen operation and display the result
    result = perform_operation(choice, num1, num2)
    print(f"Result: {result}")
    
except ValueError:
    print("Invalid input. Please enter numeric values for the numbers.")

#