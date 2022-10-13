while True:
    destination = input()
    if destination == "End":
        break
    else:
        min_needed_budget = float(input())
        available_money = 0
        while available_money < min_needed_budget:
            save_money = float(input())
            available_money += save_money
            if available_money >= min_needed_budget:
                print(f"Going to {destination}!")
                break
            else:
                continue


# destination = input()
# while destination != "End":
#     min_needed_money = float(input())
#     available_money = 0
#     while available_money < min_needed_money:
#         save_money = float(input())
#         available_money += save_money
#     print(f"Going to {destination}!")
#     destination = input()
