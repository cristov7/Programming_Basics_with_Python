number = int(input())
all_is_printed = False
counter = 1
for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(counter, end=" ")
        counter += 1
        if counter > number:
            all_is_printed = True
            break
        else:
            continue
    if all_is_printed:   # if all_is_printed == True
        break
    else:
        print()


# number = int(input())
# counter = 1
# for row in range(1, number + 1):
#     for column in range(1, row + 1):
#         print(counter, end=" ")
#         counter += 1
#         if counter > number:
#             break
#         else:
#             continue
#     if counter > number:
#         break
#     else:
#         print()
