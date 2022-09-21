# Проверява дали всички двойки имат еднаква стойност или печата максималната разлика между две последователни двойки!
number = int(input())
prev_sum = 0
max_diff = 0
for numbers in range(1, number + 1):
    number_1 = int(input())
    number_2 = int(input())
    sum_numbers = number_1 + number_2
    if numbers == 1:
        prev_sum = sum_numbers
        continue
    else:
        diff = abs(sum_numbers - prev_sum)
        if diff > max_diff:
            max_diff = diff
        else:
            prev_sum = sum_numbers
            continue
if max_diff == 0:
    print(f"Yes, value={prev_sum}")
else:
    print(f"No, maxdiff={max_diff}")


# Проверява дали всички двойки имат еднаква стойност или печата максималната разлика между всички двойки!
# import sys
# max_sum_numbers = -sys.maxsize
# min_sum_numbers = sys.maxsize
#
# number = int(input())
# for numbers in range(number):
#     number_1 = int(input())
#     number_2 = int(input())
#     sum_numbers = number_1 + number_2
#
#     if sum_numbers > max_sum_numbers:
#         max_sum_numbers = sum_numbers
#     if sum_numbers < min_sum_numbers:
#         min_sum_numbers = sum_numbers
#
# if max_sum_numbers == min_sum_numbers:
#     print(f"Yes, value={max_sum_numbers}")
# else:
#     diff = abs(max_sum_numbers - min_sum_numbers)
#     print(f"No, maxdiff={diff}")
