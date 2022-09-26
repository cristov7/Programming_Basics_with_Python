count_valid_operation = 0
number = int(input())
for x1 in range(0, number + 1):   # (number + 1):
    for x2 in range(0, number + 1):   # (number + 1):
        for x3 in range(0, number + 1):   # (number + 1):
            if x1 + x2 + x3 == number:
                count_valid_operation += 1
            else:
                continue
print(count_valid_operation)
