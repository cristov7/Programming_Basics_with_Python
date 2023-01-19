start_number = int(input())
end_number = int(input())
invalid_digit = "0"
for number in range(1000, 10000):
    number_as_string = str(number)
    if invalid_digit in number_as_string:
        continue
    else:
        first_digit_as_integer = int(number_as_string[0])
        second_digit_as_integer = int(number_as_string[1])
        third_digit_as_integer = int(number_as_string[2])
        fourth_digit_as_integer = int(number_as_string[3])
        if (first_digit_as_integer < start_number) \
                or (second_digit_as_integer < start_number) \
                or (third_digit_as_integer < start_number) \
                or (fourth_digit_as_integer < start_number) \
                or (first_digit_as_integer > end_number) \
                or (second_digit_as_integer > end_number) \
                or (third_digit_as_integer > end_number) \
                or (fourth_digit_as_integer > end_number):
            continue
        else:
            if (first_digit_as_integer % 2 == 0 and fourth_digit_as_integer % 2) \
                    or (first_digit_as_integer % 2 and fourth_digit_as_integer % 2 == 0):
                if first_digit_as_integer > fourth_digit_as_integer:
                    sum_second_and_third_digits = second_digit_as_integer + third_digit_as_integer
                    if sum_second_and_third_digits % 2 == 0:
                        print(number, end=" ")
                    else:
                        continue
                else:
                    continue
            else:
                continue


# start_num = int(input())
# finish_num = int(input())
# for number1 in range(start_num, finish_num + 1):
#     for number2 in range(start_num, finish_num + 1):
#         for number3 in range(start_num, finish_num + 1):
#             for number4 in range(start_num, finish_num + 1):
#                 if number1 % 2 == 0 and number4 % 2 != 0 or number1 % 2 != 0 and number4 % 2 == 0:
#                     if number1 > number4 and (number2 + number3) % 2 == 0:
#                         print(f"{number1}{number2}{number3}{number4}", end=" ")
