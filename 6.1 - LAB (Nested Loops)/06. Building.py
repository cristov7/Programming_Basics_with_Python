count_floors = int(input())
count_apartments_per_floor = int(input())
floor_letter = ""
for floor in range(count_floors, 0, - 1):
    for apartment in range(count_apartments_per_floor):   # (0, count_apartments_per_floor)
        if floor == count_floors:
            floor_letter = "L"
        elif floor % 2 == 0:
            floor_letter = "O"
        else:
            floor_letter = "A"
        print(f"{floor_letter}{floor}{apartment}", end=" ")
    print()
