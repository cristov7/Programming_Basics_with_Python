start_letter = input()
end_letter = input()
break_letter = input()
ord_start_letter = ord(start_letter)
ord_end_letter = ord(end_letter)
ord_break_letter = ord(break_letter)
first_letter = ""
second_letter = ""
third_letter = ""
count_combinations = 0
for ord_first_letter in range(ord_start_letter, ord_end_letter + 1):
    for ord_second_letter in range(ord_start_letter, ord_end_letter + 1):
        for ord_third_letter in range(ord_start_letter, ord_end_letter + 1):
            if ord_first_letter != ord_break_letter \
                    and ord_second_letter != ord_break_letter \
                    and ord_third_letter != ord_break_letter:
                first_letter = chr(ord_first_letter)
                second_letter = chr(ord_second_letter)
                third_letter = chr(ord_third_letter)
                print(f"{first_letter}{second_letter}{third_letter}", end=" ")
                count_combinations += 1
            else:
                continue
print(count_combinations)
