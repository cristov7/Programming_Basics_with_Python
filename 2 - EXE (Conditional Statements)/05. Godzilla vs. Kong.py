budget_for_movie = float(input())
count_supernumerary = int(input())
price_clothes_per_one_supernumerary = float(input())
decor_for_movie = budget_for_movie * 0.10
full_price_clothes_per_all_supernumerary = count_supernumerary * price_clothes_per_one_supernumerary
discount = 0
if count_supernumerary > 150:
    discount = full_price_clothes_per_all_supernumerary * 0.10
expenses_for_clothes_and_decor = full_price_clothes_per_all_supernumerary + decor_for_movie - discount
if expenses_for_clothes_and_decor > budget_for_movie:
    not_enough_money = abs(expenses_for_clothes_and_decor - budget_for_movie)
    print("Not enough money!")
    print(f"Wingard needs {not_enough_money:.2f} leva more.")
else:
    money_left_over = abs(expenses_for_clothes_and_decor - budget_for_movie)
    print("Action!")
    print(f"Wingard starts filming with {money_left_over:.2f} leva left.")
