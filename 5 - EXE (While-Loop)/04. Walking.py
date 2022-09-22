target_steps_per_day = 10000
steps_per_day = 0
while True:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        steps_per_day += steps_to_home
        if steps_per_day >= target_steps_per_day:
            steps_over_the_target = abs(steps_per_day - target_steps_per_day)
            print("Goal reached! Good job!")
            print(f"{steps_over_the_target} steps over the goal!")
            break
        else:
            needed_more_steps = abs(steps_per_day - target_steps_per_day)
            print(f"{needed_more_steps} more steps to reach goal.")
            break
    else:
        steps = int(command)
        steps_per_day += steps
        if steps_per_day >= target_steps_per_day:
            steps_over_the_target = abs(steps_per_day - target_steps_per_day)
            print("Goal reached! Good job!")
            print(f"{steps_over_the_target} steps over the goal!")
            break
        else:
            continue
