first_num_max = int(input())
second_num_max = int(input())
third_num_max = int(input())
for first_digit in range(2, first_num_max + 1):
    if first_digit % 2 != 0:
        continue
    for second_digit in range(2, second_num_max + 1):
        if second_digit == 4:
            continue
        for third_digit in range(2, third_num_max + 1):
            if third_digit % 2 != 0:
                continue
            print(f"{first_digit} {second_digit} {third_digit}")
