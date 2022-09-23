days_to_birthday = 5
pocket_money = float(input())
earn_money_from_sells_per_day = float(input())
expenses_per_whole_period = float(input())
price_per_gift = float(input())
save_money = 0
for days in range(1, days_to_birthday + 1):
    save_money += pocket_money + earn_money_from_sells_per_day
last_money = save_money - expenses_per_whole_period
if last_money >= price_per_gift:
    print(f"Profit: {last_money:.2f} BGN, the gift has been purchased.")
else:
    needed_more_money = abs(last_money - price_per_gift)
    print(f"Insufficient money: {needed_more_money:.2f} BGN.")
