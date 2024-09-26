

age = int(input("Please enter an age: "))
if age < 10 or age > 20:  # Use 'or' to check for ages outside the range
    age1 = int(input("Enter an age between 11 and 18: "))  # Missing closing parenthesis
elif age >= 10 and age <= 19:  # Corrected the missing colon here
    print("Valid age :D")