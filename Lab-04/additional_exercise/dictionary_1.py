n = int(input("Enter n: "))
dictionary = dict()

for x in range(n):
    key = input()
    value = input()
    dictionary[key] = value

m = int(input("Enter m: "))
m_list = [input() for x in range(m)]

for x in list(dictionary):
    for y in range(len(m_list)):
        if x == m_list[y]:
            m_list[y] = dictionary[x]
            del dictionary[x]

print(f"Dictionary: {dictionary}")
print(f"List: {m_list}")
