number = int(input("Enter a number: "))
list_1 = []
dict_1 = {}

for i in range(1, number):
    list_1.append(i)


for i in list_1:
    dict_1[i] = list_1[len(list_1) - i]


print(f"List: {list_1}")
print(f"Dictionary: {dict_1}")
