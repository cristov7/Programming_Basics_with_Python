width_per_cake = int(input())
length_per_cake = int(input())
amount_per_cake = width_per_cake * length_per_cake
length_per_one_piece_of_cake = 1
width_per_one_piece_of_cake = 1
amount_per_one_piece_of_cake = length_per_one_piece_of_cake * width_per_one_piece_of_cake
max_count_pieces_of_cake = amount_per_cake // amount_per_one_piece_of_cake
count_pieces = 0
while True:
    command = input()
    if command == "STOP":
        left_count_pieces = max_count_pieces_of_cake
        print(f"{left_count_pieces} pieces are left.")
        break
    else:
        count_pieces = int(command) * amount_per_one_piece_of_cake
        if count_pieces <= max_count_pieces_of_cake:
            max_count_pieces_of_cake -= count_pieces
        else:
            needed_more_pieces = abs(count_pieces - max_count_pieces_of_cake)
            print(f"No more cake left! You need {needed_more_pieces} pieces more.")
            break
