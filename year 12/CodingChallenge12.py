Year = input("Please enter a year: ")

LeapYear = False

# Check if the year is divisible by 4
if ((Year, 4) == 0):
    LeapYear = True


# Check if the year is divisible by 100
if ((Year, 100) == 0):
    LeapYear = True


# Check if the year is divisible by 400
if ((Year, 400) == 0):
    LeapYear = True

# Output the appropriate message
if (LeapYear == True):
    print(Year + " is a Leap Year")
else:
    print(Year + " is not a Leap Year")