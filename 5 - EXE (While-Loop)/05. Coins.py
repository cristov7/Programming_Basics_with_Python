change = float(input())   # лв.
change_in_coins = change * 100   # лв. в стотинки -> ( 1 лв. = 100 стотинки)
count_coins = 0
while True:
    if change_in_coins >= 200:   # 2 лв.
        count_coins += 1
        change_in_coins -= 200
    elif change_in_coins >= 100:   # 1 лв.
        count_coins += 1
        change_in_coins -= 100
    elif change_in_coins >= 50:   # 0.50 лв.
        count_coins += 1
        change_in_coins -= 50
    elif change_in_coins >= 20:   # 0.20 лв.
        count_coins += 1
        change_in_coins -= 20
    elif change_in_coins >= 10:   # 0.10 лв.
        count_coins += 1
        change_in_coins -= 10
    elif change_in_coins >= 5:   # 0.05 лв.
        count_coins += 1
        change_in_coins -= 5
    elif change_in_coins >= 2:   # 0.02 лв.
        count_coins += 1
        change_in_coins -= 2
    elif change_in_coins >= 1:   # 0.01 лв.
        count_coins += 1
        change_in_coins -= 1
    else:
        print(count_coins)
        break
