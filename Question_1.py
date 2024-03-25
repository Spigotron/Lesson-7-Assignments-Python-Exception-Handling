# Task 1

while True:
    try:
        temp = int(input("In Fahrenheit, what is the temperature? "))
        break
    except ValueError:
        print("Sorry, that's not a temperature! Please enter a valid number.")

# Tasks 2 & 3
        
def convert(temp):
    try:
        converted_temp = (temp - 32) * (5 / 9)
    except ZeroDivisionError:
        print("Sorry, you cannot divide by zero. Please try again.")
    except OverflowError:
        print("Sorry, we encountered an overflow error. Please try again.")
    else:
        print(f"In Celsius, the temperature is {converted_temp}.")
    finally:
        print("Thank you for using our weather forecast application. Have a nice day!")

convert(temp)