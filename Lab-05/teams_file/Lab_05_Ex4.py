import random
number = input("Enter a number: ")
ls_1 = list()

for i in range(6):
    numbers = random.randint(1, 10)
    ls_1.append(numbers)


def list_number(ls1, num):
    for i in range(len(ls1)):
        if ls1[i] > int(num):
            ls1[i] = 0
    return ls1


print(f"First list: {ls_1}")
print(f"Result list: {list_number(ls_1,number)}")

