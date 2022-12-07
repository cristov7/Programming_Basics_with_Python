count_locations = int(input())
sum_produce_gold_per_location = 0
for location in range(1, count_locations + 1):
    target_average_produce_gold_per_location = float(input())
    working_days_per_location = int(input())
    for day in range(1, working_days_per_location + 1):
        produce_gold_per_day = float(input())
        sum_produce_gold_per_location += produce_gold_per_day
        if day == working_days_per_location:
            average_produce_gold_per_location = sum_produce_gold_per_location / working_days_per_location
            if average_produce_gold_per_location >= target_average_produce_gold_per_location:
                print(f"Good job! Average gold per day: {average_produce_gold_per_location:.2f}.")
                sum_produce_gold_per_location = 0
            else:
                need_more_gold = abs(average_produce_gold_per_location - target_average_produce_gold_per_location)
                print(f"You need {need_more_gold:.2f} gold.")
                sum_produce_gold_per_location = 0
        else:
            continue
