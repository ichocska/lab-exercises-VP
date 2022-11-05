number = int(input("Enter a number: "))

for i in range(number):
    print("*", end='')
    for j in range(i):
        print("*", end='')
    print()
