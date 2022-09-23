type_of_flowers = input()
count_flowers = int(input())
budget = int(input())
price_per_one_rose = 5
price_per_one_dahlia = 3.80
price_per_one_tulip = 2.80
price_per_one_narcissus = 3
price_per_one_gladiolus = 2.50
discount = 0
full_price_per_flowers = 0
if type_of_flowers == "Roses":
    if count_flowers > 80:
        discount = (count_flowers * price_per_one_rose) * 0.10
        full_price_per_flowers = (count_flowers * price_per_one_rose) - discount
    else:
        full_price_per_flowers = count_flowers * price_per_one_rose
elif type_of_flowers == "Dahlias":
    if count_flowers > 90:
        discount = (count_flowers * price_per_one_dahlia) * 0.15
        full_price_per_flowers = (count_flowers * price_per_one_dahlia) - discount
    else:
        full_price_per_flowers = count_flowers * price_per_one_dahlia
elif type_of_flowers == "Tulips":
    if count_flowers > 80:
        discount = (count_flowers * price_per_one_tulip) * 0.15
        full_price_per_flowers = (count_flowers * price_per_one_tulip) - discount
    else:
        full_price_per_flowers = count_flowers * price_per_one_tulip
elif type_of_flowers == "Narcissus":
    if count_flowers < 120:
        discount = (count_flowers * price_per_one_narcissus) * 0.15
        full_price_per_flowers = (count_flowers * price_per_one_narcissus) + discount
    else:
        full_price_per_flowers = count_flowers * price_per_one_narcissus
elif type_of_flowers == "Gladiolus":
    if count_flowers < 80:
        discount = (count_flowers * price_per_one_gladiolus) * 0.20
        full_price_per_flowers = (count_flowers * price_per_one_gladiolus) + discount
    else:
        full_price_per_flowers = count_flowers * price_per_one_gladiolus
if budget >= full_price_per_flowers:
    money_left_over = abs(budget - full_price_per_flowers)
    print(f"Hey, you have a great garden with {count_flowers} {type_of_flowers} and {money_left_over:.2f} leva left.")
else:
    needed_more_money = abs(budget - full_price_per_flowers)
    print(f"Not enough money, you need {needed_more_money:.2f} leva more.")
