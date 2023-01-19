number = int(input())
end_range = 0
if number > 10:
    end_range = 10
else:
    end_range = number
valid_digits_list = [digit for digit in range(1, end_range)]
for current_number in range(1000, 10000):
    current_number_as_string = str(current_number)
    first_digit_as_integer = int(current_number_as_string[0])
    second_digit_as_integer = int(current_number_as_string[1])
    third_digit_as_integer = int(current_number_as_string[2])
    fourth_digit_as_integer = int(current_number_as_string[3])
    if fourth_digit_as_integer in valid_digits_list \
            and second_digit_as_integer in valid_digits_list \
            and third_digit_as_integer in valid_digits_list \
            and first_digit_as_integer in valid_digits_list:
        first_sum = first_digit_as_integer + second_digit_as_integer
        second_sum = third_digit_as_integer + fourth_digit_as_integer
        if first_sum == second_sum:
            if number % first_sum == 0:
                print(current_number, end=" ")
            else:
                continue
        else:
            continue
    else:
        continue


# input_number = int(input())
# if input_number > 10:
#     number = 10
# else:
#     number = input_number
# for num01 in range(1, number):
#     for num02 in range(1, number):
#         for num03 in range(1, number):
#             for num04 in range(1, number):
#                 if (num01 + num02) == (num03 + num04) and input_number % (num01 + num02) == 0:
#                     print(f"{num01}{num02}{num03}{num04}", end=" ")
