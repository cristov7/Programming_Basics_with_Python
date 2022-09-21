from math import floor
count_played_tournaments = int(input())
starting_points_of_the_leaderboard = int(input())
points_from_all_tournaments = 0
count_winning_tournaments = 0
for tournaments in range(count_played_tournaments):
    tournament_stage_reached = input()
    if tournament_stage_reached == "W":
        count_winning_tournaments += 1
        points_from_tournament = 2000
        points_from_all_tournaments += points_from_tournament
    elif tournament_stage_reached == "F":
        points_from_tournament = 1200
        points_from_all_tournaments += points_from_tournament
    elif tournament_stage_reached == "SF":
        points_from_tournament = 720
        points_from_all_tournaments += points_from_tournament
total_points = starting_points_of_the_leaderboard + points_from_all_tournaments
average_winning_points_from_tournament = points_from_all_tournaments / count_played_tournaments
percent_winning_tournaments = (count_winning_tournaments / count_played_tournaments) * 100
print(f"Final points: {total_points}")
print(f"Average points: {floor(average_winning_points_from_tournament)}")
print(f"{percent_winning_tournaments:.2f}%")
