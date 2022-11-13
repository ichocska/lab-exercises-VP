import random
list_1 = []
list_2 = []
sum_of_elements = 0

for i in range(5):
    numbers = random.randint(1, 10)
    list_1.append(numbers)

list_2.append(list_1[0])

for i in range(len(list_1) - 1):
    sum_of_elements = list_1[i] + list_1[i + 1]
    list_2.append(sum_of_elements)
    list_2.append(list_1[i + 1])


print(f"List_1: {list_1}")
print(f"List_2: {list_2}")