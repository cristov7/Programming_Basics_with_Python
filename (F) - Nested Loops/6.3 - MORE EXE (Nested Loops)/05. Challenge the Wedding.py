count_man = int(input())
count_women = int(input())
max_count_tables = int(input())
finish_program = False
for men in range(1, count_man + 1):
    if finish_program:
        break
    else:
        for woman in range(1, count_women + 1):
            if max_count_tables > 0:
                print(f"({men} <-> {woman})", end=" ")
                max_count_tables -= 1
            else:
                finish_program = True
                break


# man_qty = int(input())
# women_qty = int(input())
# max_table = int(input())
# counter_table = 0
# for man in range(1, man_qty + 1):
#     for women in range(1, women_qty + 1):
#         if counter_table < max_table:
#             print(f"({man} <-> {women})", end=" ")
#             counter_table += 1
