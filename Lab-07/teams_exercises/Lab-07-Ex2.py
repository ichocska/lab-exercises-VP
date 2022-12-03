from math import sqrt
try:
    number = int(input("Enter a number: "))
    print(f"Result: {sqrt(number)}")
except ValueError:
    print("Invalid number")
finally:
    print("Good Bye")