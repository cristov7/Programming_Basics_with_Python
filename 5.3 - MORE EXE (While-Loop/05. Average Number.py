number = int(input())
sum_current_numbers = 0
for numbers in range(number):
    current_number = int(input())
    sum_current_numbers += current_number
else:
    average = sum_current_numbers / number
    print(f"{average:.2f}")
