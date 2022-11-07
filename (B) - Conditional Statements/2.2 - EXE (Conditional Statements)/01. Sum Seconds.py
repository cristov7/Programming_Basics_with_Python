player_1_finishing_in_seconds = int(input())
player_2_finishing_in_seconds = int(input())
player_3_finishing_in_seconds = int(input())
sum_seconds = player_1_finishing_in_seconds + player_2_finishing_in_seconds + player_3_finishing_in_seconds
minutes = sum_seconds // 60
seconds = sum_seconds % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
