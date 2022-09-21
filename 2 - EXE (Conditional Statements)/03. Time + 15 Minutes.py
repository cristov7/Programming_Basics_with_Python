hours = int(input())
minutes = int(input())
hours_in_minutes = hours * 60
bonus_minutes = 15
sum_minutes = minutes + hours_in_minutes + bonus_minutes
new_time_in_hours = (sum_minutes // 60) % 24
new_time_in_minutes = sum_minutes % 60
if new_time_in_minutes < 10:
    print(f"{new_time_in_hours}:0{new_time_in_minutes}")
else:
    print(f"{new_time_in_hours}:{new_time_in_minutes}")
