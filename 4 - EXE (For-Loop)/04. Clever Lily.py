age_per_Lilly = int(input())
price_per_wash_machine = float(input())
price_per_one_toy = int(input())
toys_from_birthdays = 0
money_from_birthdays = 0
more_money_per_next_birthday = 0
minus_money = 0
for birthdays in range(1, age_per_Lilly + 1):
    if birthdays % 2 != 0:
        toys_from_birthdays += 1
    else:
        more_money_per_next_birthday += 10
        money_from_birthdays += more_money_per_next_birthday
        minus_money += 1
money_from_sell_toys = toys_from_birthdays * price_per_one_toy
save_money_from_birthdays = money_from_birthdays - minus_money
available_money = money_from_sell_toys + save_money_from_birthdays
if available_money >= price_per_wash_machine:
    money_left_over = abs(available_money - price_per_wash_machine)
    print(f"Yes! {money_left_over:.2f}")
else:
    not_enough_money = abs(available_money - price_per_wash_machine)
    print(f"No! {not_enough_money:.2f}")
