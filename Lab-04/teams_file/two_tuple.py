number = input("Enter a number: ")

tuple_1 = tuple(number)
new_number = int(number[::-1])
tuple_2 = tuple(str(new_number))


print(f"Tuple 1: {tuple_1}")
print(f"Tuple 2: {tuple_2}")


