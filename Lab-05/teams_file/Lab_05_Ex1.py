option = input("Enter a figure: ")


def square(a):
    area = a * a
    return area


def rectangle(a, b):
    area = a * b
    return area


def triangle(a, b):
    area = (a * b) / 2
    return area


if option == "square":
    a = float(input("Enter a number: "))
    print(f"Area = {square(a)}")
elif option == "rectangle":
    a = float(input("Enter a number for a: "))
    b = float(input("Enter a number for b: "))
    print(f"Area = {rectangle(a, b)}")
elif option == "triangle":
    a = float(input("Enter a number for a: "))
    b = float(input("Enter a number for b: "))
    print(f"Area = {triangle(a, b)}")
