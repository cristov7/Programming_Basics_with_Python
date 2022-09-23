most_goals = 0
best_player_name = ""
while True:
    player_name = input()
    if player_name == "END":
        print(f"{best_player_name} is the best player!")
        if most_goals >= 3:
            print(f"He has scored {most_goals} goals and made a hat-trick !!!")
            break
        else:
            print(f"He has scored {most_goals} goals.")
            break
    else:
        scored_goals = int(input())
        if scored_goals >= 10:
            best_player_name = player_name
            most_goals = scored_goals
            print(f"{best_player_name} is the best player!")
            print(f"He has scored {most_goals} goals and made a hat-trick !!!")
            break
        else:
            if scored_goals > most_goals:
                most_goals = scored_goals
                best_player_name = player_name
            else:
                continue
