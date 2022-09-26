start_number = int(input())
final_number = int(input())
magic_number = int(input())
count_combination = 0
combination_is_found = False
for start_numbers in range(start_number, final_number + 1):
    for final_numbers in range(start_number, final_number + 1):
        count_combination += 1
        if start_numbers + final_numbers == magic_number:
            combination_is_found = True
            break
        else:
            continue
    if combination_is_found:   # if combination_is_found == True:
        break
    else:
        continue
if combination_is_found:   # if combination_is_found == True:
    print(f"Combination N:{count_combination} ({start_numbers} + {final_numbers} = {magic_number})")
else:
    print(f"{count_combination} combinations - neither equals {magic_number}")


# start_number = int(input())
# final_number = int(input())
# magic_number = int(input())
# count_combination = 0
# for start_numbers in range(start_number, final_number + 1):
#     for final_numbers in range(start_number, final_number + 1):
#         count_combination += 1
#         if start_numbers + final_numbers == magic_number:
#             break
#         else:
#             continue
#     if start_numbers + final_numbers == magic_number:
#         break
#     else:
#         continue
# if start_numbers + final_numbers == magic_number:
#     print(f"Combination N:{count_combination} ({start_numbers} + {final_numbers} = {magic_number})")
# else:
#     print(f"{count_combination} combinations - neither equals {magic_number}")
