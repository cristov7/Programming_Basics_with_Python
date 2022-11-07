N1 = int(input())
N2 = int(input())
operator = input()
if operator == "+":
    result = N1 + N2
    if result % 2 == 0:
        even_or_odd = "even"
        print(f"{N1} {operator} {N2} = {result} - {even_or_odd}")
    else:
        even_or_odd = "odd"
        print(f"{N1} {operator} {N2} = {result} - {even_or_odd}")
elif operator == "-":
    result = N1 - N2
    if result % 2 == 0:
        even_or_odd = "even"
        print(f"{N1} {operator} {N2} = {result} - {even_or_odd}")
    else:
        even_or_odd = "odd"
        print(f"{N1} {operator} {N2} = {result} - {even_or_odd}")
elif operator == "*":
    result = N1 * N2
    if result % 2 == 0:
        even_or_odd = "even"
        print(f"{N1} {operator} {N2} = {result} - {even_or_odd}")
    else:
        even_or_odd = "odd"
        print(f"{N1} {operator} {N2} = {result} - {even_or_odd}")
elif operator == "/":
    if N2 != 0:
        result = N1 / N2
        print(f"{N1} {operator} {N2} = {result:.2f}")
    else:
        print(f"Cannot divide {N1} by zero")
elif operator == "%":
    if N2 != 0:
        result = N1 % N2
        print(f"{N1} {operator} {N2} = {result}")
    else:
        print(f"Cannot divide {N1} by zero")
