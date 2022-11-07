count_rest_days = int(input())
one_year_in_days = 365
count_work_days = one_year_in_days - count_rest_days
max_time_to_play_per_year_in_minutes = 30000
time_to_play_in_a_rest_day = 127
time_to_play_in_a_work_day = 63
time_to_play_in_rest_days_per_one_year_in_minutes = count_rest_days * time_to_play_in_a_rest_day
time_to_play_in_work_days_per_one_year_in_minutes = count_work_days * time_to_play_in_a_work_day
time_to_play_per_one_year_in_minutes = time_to_play_in_rest_days_per_one_year_in_minutes + time_to_play_in_work_days_per_one_year_in_minutes
if time_to_play_per_one_year_in_minutes > max_time_to_play_per_year_in_minutes:
    print("Tom will run away")
    diff_in_minutes = abs(time_to_play_per_one_year_in_minutes - max_time_to_play_per_year_in_minutes)
    hours = diff_in_minutes // 60
    minutes = diff_in_minutes % 60
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    diff_in_minutes = abs(time_to_play_per_one_year_in_minutes - max_time_to_play_per_year_in_minutes)
    hours = diff_in_minutes // 60
    minutes = diff_in_minutes % 60
    print(f"{hours} hours and {minutes} minutes less for play")
