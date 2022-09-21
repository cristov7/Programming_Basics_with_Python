count_moves_to_play = int(input())
result = 0
count_times_between_0_and_9 = 0
count_times_between_10_and_19 = 0
count_times_between_20_and_29 = 0
count_times_between_30_and_39 = 0
count_times_between_40_and_50 = 0
count_times_invalid_numbers = 0
for every_move in range(count_moves_to_play):
    move = int(input())
    if 0 <= move <= 9:
        count_times_between_0_and_9 += 1
        points = move * 0.20
        result += points
    elif 10 <= move <= 19:
        count_times_between_10_and_19 += 1
        points = move * 0.30
        result += points
    elif 20 <= move <= 29:
        count_times_between_20_and_29 += 1
        points = move * 0.40
        result += points
    elif 30 <= move <= 39:
        count_times_between_30_and_39 += 1
        points = 50
        result += points
    elif 40 <= move <= 50:
        count_times_between_40_and_50 += 1
        points = 100
        result += points
    else:
        count_times_invalid_numbers += 1
        result /= 2
percent_count_times_between_0_and_9 = (count_times_between_0_and_9 / count_moves_to_play) * 100
percent_count_times_between_10_and_19 = (count_times_between_10_and_19 / count_moves_to_play) * 100
percent_count_times_between_20_and_29 = (count_times_between_20_and_29 / count_moves_to_play) * 100
percent_count_times_between_30_and_39 = (count_times_between_30_and_39 / count_moves_to_play) * 100
percent_count_times_between_40_and_50 = (count_times_between_40_and_50 / count_moves_to_play) * 100
percent_count_times_invalid_numbers = (count_times_invalid_numbers / count_moves_to_play) * 100
print(f"{result:.2f}")
print(f"From 0 to 9: {percent_count_times_between_0_and_9:.2f}%")
print(f"From 10 to 19: {percent_count_times_between_10_and_19:.2f}%")
print(f"From 20 to 29: {percent_count_times_between_20_and_29:.2f}%")
print(f"From 30 to 39: {percent_count_times_between_30_and_39:.2f}%")
print(f"From 40 to 50: {percent_count_times_between_40_and_50:.2f}%")
print(f"Invalid numbers: {percent_count_times_invalid_numbers:.2f}%")
