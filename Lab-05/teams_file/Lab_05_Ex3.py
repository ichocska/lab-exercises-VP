operation = input("Enter a valid operation: ")
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))


def calculator(num_1, num_2):
    if operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    elif operation == "*":
        return num_1 * num_2
    elif operation == "/":
        return num_1 / num_2
    else:
        print("Not a valid operation")


print(f"Result = {calculator(num1, num2)}")