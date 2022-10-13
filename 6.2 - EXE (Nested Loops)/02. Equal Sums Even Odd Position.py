first_number = int(input())
second_number = int(input())
for numbers in range(first_number, second_number + 1):
    odd_value_sum = 0
    even_value_sum = 0
    numbers_as_string = str(numbers)
    for index, value in enumerate(numbers_as_string):
        if index % 2 == 0:
            odd_value_sum += int(value)
        else:
            even_value_sum += int(value)
    if odd_value_sum == even_value_sum:
        print(numbers, end=" ")
    else:
        continue


# first_number = int(input())
# second_number = int(input())
# for numbers in range(first_number, second_number + 1):
#     numbers = str(numbers)
#     odd_value_sum = int(numbers[0]) + int(numbers[2]) + int(numbers[4])
#     even_value_sum = int(numbers[1]) + int(numbers[3]) + int(numbers[5])
#     if odd_value_sum == even_value_sum:
#         print(numbers, end=" ")
#     else:
#         continue
