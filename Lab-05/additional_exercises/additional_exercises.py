#Exercise 1
def input_nums(n):
    ls_1 = list()
    if type(n) != int:
        if n.isnumeric():
            n = int(n)
        else:
            return ls_1
    for i in range(n):
        num = input("Enter a list element: ")
        if num.isnumeric():
            ls_1.append(int(num))
        else:
            continue
    return ls_1


#number = input("How many numbers: ")
#print(input_nums(number))


def sum_list(lst):
    sum_of_elements = 0
    for i in lst:
        if type(i) == int or type(i) == float:
            sum_of_elements += i
        elif i.isnumeric():
            sum_of_elements += int(i)

    return sum_of_elements

#print(sum_list([1, "a", 3.14, "5"]))


def max_of_two(a, b):
    if (type(a) != int and type(a) != float) and (type(b) != int and type(b) != float):
        return
    elif type(a) != int or type(a) != float:
        return b
    elif type(b) != int or type(b) != float:
        return a
    elif int(a) > int(b):
        return a
    elif int(b) > int(a):
        return b
    elif int(a) == int(b):
        return a

#print(max_of_two(2.5, 13))

#print(max_of_two(sum_list(input_nums(4)), sum_list(input_nums(3))))
#print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))

#Exercise 2
def list_avg(lst, multiplier=1):
    if multiplier == 1:
        sum_of_elements = 0
        counter = 0
        for i in lst:
            if type(i) == int or type(i) == float:
                sum_of_elements += i
                counter += 1
            elif i.isnumeric():
                sum_of_elements += int(i)
                counter += 1
        return sum_of_elements / counter
    else:
        sum_of_elements = 0
        counter = 0
        for i in lst:
            if type(i) == int or type(i) == float:
                sum_of_elements += (i * multiplier)
                counter += 1
            elif i.isnumeric():
                sum_of_elements += (int(i) * multiplier)
                counter += 1
        return sum_of_elements / counter

#print(list_avg(["1", 2.5, 3, 1.5,'b'], 2))

#Exercise 3
def digitize(num):
    ls1 = list()
    for i in num:
        if isinstance(i, str):
            if i.isnumeric():
                i = int(i)
            else:
                print("Error")
        ls1.append(i)
    tup = tuple(ls1)
    return tup
#number = input("Enter a number: ")
#a,b,c,d = digitize(number)
#print(a)
#print(b)
#print(c)
#print(d)


#Exercise 4
def get_collection_builder(col_type):
    def tuple_builder(a, b, c, d):
        return (a, b, c, d)
    def list_builder(a, b, c, d):
        return [a, b, c, d]
    def set_builder(a, b, c, d):
        return {a, b, c, d}
    if isinstance(col_type, str):
        if col_type == "tuple":
            return tuple_builder
        elif col_type == "list":
            return list_builder
        elif col_type == "set":
            return set_builder
        else:
            print("Error")


#tuple_builder = get_collection_builder("tuple")
#tuple1 = tuple_builder(1, 2.23, 3,"hi")
#list_builder = get_collection_builder("list")
#list1 = list_builder(1, 2.23, 4,"hello")
#set_builder = get_collection_builder("set")
#set1 = set_builder(1,2,3,'asd')
#print(f"Tuple: {tuple1}")
#print(f"List: {list1}")
#print(f"Set: {set1}")

#Exercise 5
def is_valid_triangle(a, b, c):
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int) and (a + b > c) and (a + c > b) and (b + c > a) \
    and a > 0 and b > 0 and c > 0:
        return True
    else:
        return False

#can_triangle_exist = is_valid_triangle
#print(can_triangle_exist(3,4,"5"))