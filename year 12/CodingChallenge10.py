temp = float(input("Enter a temperature: "))
humidity = int(input("Enter the humidity: "))
window = input("Is window open = 1 or closed = 2? ")
if temp > 25 or humidity > 50 and window == 1:
    print("Keep the window open.")
if temp > 25 or humidity > 50 and window == 2:
    print("Open the window")
if temp < 10  or humidity < 50 and window == 1:
    print("Close the window")
if temp < 10  or humidity < 50 and window == 2:
    print("Keep window closed.")