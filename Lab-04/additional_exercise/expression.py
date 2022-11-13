n = int(input("Enter a number: "))
expression = ""
new_number = n
sum_of_expressions = 0

for i in range(1, n + 1):
    expression += str(n) * i
    if i < n:
        expression += ' + '
    sum_of_expressions += new_number
    new_number = new_number * 10 + n

print(f"{expression} = {sum_of_expressions}")

