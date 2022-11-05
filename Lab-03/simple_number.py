import math
number = int(input("Enter a number: "))
prime_number = True


while number <= 0:
    print("Provided number is incorrect")
    number = int(input("Enter a number: "))

for i in range(2, int(math.sqrt(number)) + 1):
    if number % 2 == 0:
        prime_number = False

if prime_number and number > 1:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
