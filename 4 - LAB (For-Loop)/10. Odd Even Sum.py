n = int(input())
even_numbers_sum = 0
odd_numbers_sum = 0
for numbers in range(n):
    if numbers % 2 == 0:
        even_number = int(input())
        even_numbers_sum += even_number
    else:
        odd_number = int(input())
        odd_numbers_sum += odd_number
if even_numbers_sum == odd_numbers_sum:
    print("Yes")
    print(f"Sum = {even_numbers_sum}")
else:
    diff = abs(even_numbers_sum - odd_numbers_sum)
    print("No")
    print(f"Diff = {diff}")
