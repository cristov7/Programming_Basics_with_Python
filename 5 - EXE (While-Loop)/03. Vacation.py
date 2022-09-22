price_per_excursion = float(input())
available_money = float(input())
days = 0
spend_days_in_a_row = 0
while True:
    command = input()   # "spend" / "save"
    days += 1
    if command == "spend":
        spend_days_in_a_row += 1
        if spend_days_in_a_row == 5:
            print("You can't save the money.")
            print(f"{days}")
            break
        else:
            spend_money = float(input())
            if spend_money > available_money:
                available_money = 0
            else:
                available_money -= spend_money
    elif command == "save":
        spend_days_in_a_row = 0
        save_money = float(input())
        available_money += save_money
        if available_money >= price_per_excursion:
            print(f"You saved the money for {days} days.")
            break
        else:
            continue
    else:
        continue
