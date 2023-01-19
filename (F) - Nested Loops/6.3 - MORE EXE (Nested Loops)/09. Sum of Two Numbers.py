start = int(input())
stop = int(input())
magic_number = int(input())
counter = 0
is_found = False
first_number = 0
second_number = 0
for first_number in range(start, stop + 1):
    for second_number in range(start, stop + 1):
        counter += 1
        if first_number + second_number == magic_number:
            is_found = True
            break
        else:
            continue
    if is_found:
        break
    else:
        continue
if is_found:
    print(f"Combination N:{counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")
