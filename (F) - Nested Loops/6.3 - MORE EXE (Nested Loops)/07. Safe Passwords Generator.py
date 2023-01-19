a = int(input())
b = int(input())
max_quantity = int(input())
A = 35
B = 64
counter = 0
for some_a in range(1, a + 1):
    for some_b in range(1, b + 1):
        if max_quantity <= counter:
            break
        else:
            print(f"{chr(A)}{chr(B)}{some_a}{some_b}{chr(B)}{chr(A)}", end="|")
            counter += 1
            if A >= 55:
                A = 35
            else:
                A += 1
            if B >= 96:
                B = 64
            else:
                B += 1
