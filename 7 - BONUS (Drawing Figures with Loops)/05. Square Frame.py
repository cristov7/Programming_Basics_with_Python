number = int(input())
counter = 2
if number == 1:
    print("+")
else:
    for first_row in range(1, number + 1):
        if first_row == 1:
            print("+", end=" ")
        elif first_row == number:
            print("+")
            break
        else:
            print("-", end=" ")
    while counter < number:
        counter += 1
        for next_rows in range(1, number + 1):
            if next_rows == 1:
                print("|", end=" ")
            elif next_rows == number:
                print("|")
            else:
                print("-", end=" ")
    for last_row in range(1, number + 1):
        if last_row == 1:
            print("+", end=" ")
        elif last_row == number:
            print("+")
            break
        else:
            print("-", end=" ")
