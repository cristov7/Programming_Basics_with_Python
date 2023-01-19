max_first_number = int(input())
max_second_number = int(input())
max_third_number = int(input())
invalid_digit = "0"
valid_digits = [2, 3, 5, 7]
for number in range(100, 1000):
    number_as_string = str(number)
    first_digit_as_string = number_as_string[0]
    second_digit_as_string = number_as_string[1]
    third_digit_as_string = number_as_string[2]
    if invalid_digit == first_digit_as_string \
            or invalid_digit == second_digit_as_string \
            or invalid_digit == third_digit_as_string:
        continue
    else:
        first_digit_as_integer = int(first_digit_as_string)
        second_digit_as_integer = int(second_digit_as_string)
        third_digit_as_integer = int(third_digit_as_string)
        if first_digit_as_integer <= max_first_number \
                and second_digit_as_integer <= max_second_number \
                and third_digit_as_integer <= max_third_number:
            if first_digit_as_integer % 2 == 0 \
                    and second_digit_as_integer in valid_digits \
                    and third_digit_as_integer % 2 == 0:
                print(f"{first_digit_as_string} {second_digit_as_string} {third_digit_as_string}")
            else:
                continue
        else:
            continue


# first = int(input())
# second = int(input())
# third = int(input())
# ten = [2, 3, 5, 7]
# for i in range(2, first+1, 2):
#     for l in range(1, second + 1):
#         for j in range(2, third+1, 2):
#             if l in ten:
#                 print(i, l, j)
