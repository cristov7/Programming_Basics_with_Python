import sys
max_number = - sys.maxsize
n = int(input())
sum_numbers = 0
for numbers in range(n):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number
if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    others_num = sum_numbers - max_number
    diff = abs(max_number - others_num)
    print(f"Diff = {diff}")
