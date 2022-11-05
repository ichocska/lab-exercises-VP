numbers = int(input("Еnter the number of numbers: "))
sum = 0

for i in range(numbers):
    num = int(input("Input a number: "))
    sum += num

print(f"Sum is {sum}")