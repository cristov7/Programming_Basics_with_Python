start_sector_as_upper_letter = "A"
last_sector_as_upper_letter = input()
count_rows_in_first_sector = int(input())
count_rows_in_sector = count_rows_in_first_sector
count_rows_in_odd_row = int(input())
count_seats_in_even_row = count_rows_in_odd_row + 2
all_count_seats = 0
for sector in range(ord(start_sector_as_upper_letter), ord(last_sector_as_upper_letter) + 1):
    sector_as_upper_letter = chr(sector)
    for row in range(1, count_rows_in_sector + 1):
        row_as_digit = row
        if row % 2 == 0:
            start_seats_as_lower_letter = ord("a")
            for seat in range(start_seats_as_lower_letter, start_seats_as_lower_letter + count_seats_in_even_row):
                seat_as_lower_letter = chr(seat)
                print(f"{sector_as_upper_letter}{row_as_digit}{seat_as_lower_letter}")
                all_count_seats += 1
        else:
            start_seats_as_lower_letter = ord("a")
            for seat in range(start_seats_as_lower_letter, start_seats_as_lower_letter + count_rows_in_odd_row):
                seat_as_lower_letter = chr(seat)
                print(f"{sector_as_upper_letter}{row_as_digit}{seat_as_lower_letter}")
                all_count_seats += 1
    count_rows_in_sector += 1
print(all_count_seats)


# last_sector = ord(input())
# rows_qty = int(input())
# seats_qty = int(input())
# seats = 0
# counter = 0
# for sectors in range(65, last_sector + 1):
#     for row in range(1, rows_qty + 1):
#         if row % 2 == 0:
#             seats = seats_qty + 2
#         else:
#             seats = seats_qty
#         seat_num = 96
#         for seat in range(1, seats + 1):
#             seat_num += 1
#             print(f"{chr(sectors)}{row}{chr(seat_num)}")
#             counter += 1
#     rows_qty += 1
# print(counter)
