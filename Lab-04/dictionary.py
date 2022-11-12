input_text = input("Enter a text: ")
dict_1 = {}

for i in input_text:
    if i in dict_1:
        dict_1[i] += 1
    else:
        dict_1[i] = 1

print(f"Dictionary: {dict_1}")