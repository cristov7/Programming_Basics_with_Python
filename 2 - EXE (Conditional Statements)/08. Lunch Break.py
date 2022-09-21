from math import ceil
name_of_the_serial = input()
time_per_one_episode = int(input())
time_per_lunch_break = int(input())
time_per_lunch = time_per_lunch_break / 8
time_to_relax = time_per_lunch_break / 4
needed_time_to_do_all_things = time_per_one_episode + time_per_lunch + time_to_relax
if needed_time_to_do_all_things <= time_per_lunch_break:
    left_time = abs(needed_time_to_do_all_things - time_per_lunch_break)
    print(f"You have enough time to watch {name_of_the_serial} and left with {ceil(left_time)} minutes free time.")
else:
    needed_more_time = abs(needed_time_to_do_all_things - time_per_lunch_break)
    print(f"You don't have enough time to watch {name_of_the_serial}, you need {ceil(needed_more_time)} more minutes.")
