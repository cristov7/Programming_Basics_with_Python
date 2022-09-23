name_per_actor = input()
points_from_academy = float(input())
count_raters = int(input())
final_points = points_from_academy
for raters in range(count_raters):
    name_per_rater = input()
    points_from_rater = float(input())
    len_name = len(name_per_rater)
    points_from_competition = (len(name_per_rater) * points_from_rater) / 2
    final_points += points_from_competition
    if final_points >= 1250.5:
        print(f"Congratulations, {name_per_actor} got a nominee for leading role with {final_points:.1f}!")
        break
    else:
        continue
else:
# if final_points < 1250.5:
    more_points_for_nominee = abs(final_points - 1250.5)
    print(f"Sorry, {name_per_actor} you need {more_points_for_nominee:.1f} more!")
