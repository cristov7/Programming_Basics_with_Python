start_points = int(input())
bonus_points = 0
extra_bonus_points = 0
if start_points <= 100:
    bonus_points = 5
    if start_points % 2 == 0:
        extra_bonus_points = 1
    elif start_points % 10 == 5:
        extra_bonus_points = 2
elif start_points > 1000:
    bonus_points = start_points * 0.10
    if start_points % 2 == 0:
        extra_bonus_points = 1
    elif start_points % 10 == 5:
        extra_bonus_points = 2
elif start_points > 100:
    bonus_points = start_points * 0.20
    if start_points % 2 == 0:
        extra_bonus_points = 1
    elif start_points % 10 == 5:
        extra_bonus_points = 2
all_bonus_points = bonus_points + extra_bonus_points
sum_start_points_and_all_bonus_points = start_points + all_bonus_points
print(all_bonus_points)
print(sum_start_points_and_all_bonus_points)
