price_per_excursion = float(input())
count_puzzles = int(input())
count_speaking_dolls = int(input())
count_teddy_bears = int(input())
count_minions = int(input())
count_trucks = int(input())
price_per_one_puzzle = 2.60
price_per_one_speaking_doll = 3
price_per_one_teddy_bear = 4.10
price_per_one_minion = 8.20
price_per_one_truck = 2
full_price_per_puzzles = count_puzzles * price_per_one_puzzle
full_price_per_speaking_dolls = count_speaking_dolls * price_per_one_speaking_doll
full_price_per_teddy_bears = count_teddy_bears * price_per_one_teddy_bear
full_price_per_minions = count_minions * price_per_one_minion
full_price_per_trucks = count_trucks * price_per_one_truck
full_price_per_all = full_price_per_puzzles + full_price_per_speaking_dolls + full_price_per_teddy_bears + full_price_per_minions + full_price_per_trucks
full_count_toys = count_puzzles + count_speaking_dolls + count_teddy_bears + count_minions + count_trucks
discount = 0
if full_count_toys >= 50:
    discount = full_price_per_all * 0.25
earn_money = full_price_per_all - discount
rent = earn_money * 0.10
final_money = earn_money - rent
if final_money >= price_per_excursion:
    money_left_over = abs(final_money - price_per_excursion)
    print(f"Yes! {money_left_over:.2f} lv left.")
else:
    not_enough_money = abs(final_money - price_per_excursion)
    print(f"Not enough money! {not_enough_money:.2f} lv needed.")
