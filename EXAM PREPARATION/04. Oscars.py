name_actor = input()
points_from_academy = float(input())
count_raters = int(input())
total_points = points_from_academy
for raters in range(count_raters):
    name_rater = input()
    points_from_rater = float(input())
    full_points_from_rater = (len(name_rater) * points_from_rater) / 2
    total_points += full_points_from_rater
    if total_points > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
        break
    else:
        continue
else:
    needed_more_points = abs(total_points - 1250.5)
    print(f"Sorry, {name_actor} you need {needed_more_points:.1f} more!")
