start_number = input()
final_number = input()
from_start_number_take_first_digital = int(start_number[0])
from_start_number_take_second_digital = int(start_number[1])
from_start_number_take_third_digital = int(start_number[2])
from_start_number_take_forth_digital = int(start_number[3])
from_final_number_take_first_digital = int(final_number[0])
from_final_number_take_second_digital = int(final_number[1])
from_final_number_take_third_digital = int(final_number[2])
from_final_number_take_forth_digital = int(final_number[3])
for first_digit in range(from_start_number_take_first_digital, from_final_number_take_first_digital + 1):
    if first_digit % 2 == 0:
        continue
    for second_digit in range(from_start_number_take_second_digital, from_final_number_take_second_digital + 1):
        if second_digit % 2 == 0:
            continue
        for third_digit in range(from_start_number_take_third_digital, from_final_number_take_third_digital + 1):
            if third_digit % 2 == 0:
                continue
            for forth_digit in range(from_start_number_take_forth_digital, from_final_number_take_forth_digital + 1):
                if forth_digit % 2 == 0:
                    continue
                print(f"{first_digit}{second_digit}{third_digit}{forth_digit}", end=" ")
