max_first_digit = int(input())
max_second_digit = int(input())
max_third_digit = int(input())
for number in range(100, 1000):
    number_as_string = str(number)
    first_digit_as_integer = int(number_as_string[0])
    second_digit_as_integer = int(number_as_string[1])
    third_digit_as_integer = int(number_as_string[2])
    if first_digit_as_integer <= max_first_digit \
            and second_digit_as_integer <= max_second_digit \
            and third_digit_as_integer <= max_third_digit:
        valid_first_and_third_digits_list = [2, 4, 6, 8]
        valid_second_digits_list = [2, 3, 5, 7]
        if first_digit_as_integer in valid_first_and_third_digits_list \
                and second_digit_as_integer in valid_second_digits_list \
                and third_digit_as_integer in valid_first_and_third_digits_list:
            print(f"{first_digit_as_integer} {second_digit_as_integer} {third_digit_as_integer}")
        else:
            continue
    else:
        continue
