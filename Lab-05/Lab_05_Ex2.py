num = input("Enter a number: ")


def palindrome_number(number):
    new_number = number[::-1]
    if number == new_number:
        return 1
    else:
        return 0


print(f"{palindrome_number(num)}")