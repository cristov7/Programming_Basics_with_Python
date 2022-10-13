n = int(input())
left_sum = 0
for left_side in range(n):
    left_number = int(input())
    left_sum += left_number
right_sum = 0
for right_side in range(n):
    right_number = int(input())
    right_sum += right_number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
