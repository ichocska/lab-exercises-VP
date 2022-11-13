num = int(input('How many numbers: '))
list_1 = [int(input("Enter a number: ")) for x in range(num)]
new_number = int(input("Enter a 0 or 1: "))

if new_number == 0:
    for i in range(len(list_1)):
        if i % 2 == 0 and i != 0:
            list_1[i] += 5
    else:
        for i in range(len(list_1)):
            if i % 2 != 0:
                list_1[i] += 10

print(list_1)
