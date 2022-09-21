group_budget = int(input())
season = input()
count_fishermen = int(input())
price_per_ship_on_rent = 0
discount = 0
price_per_ship_on_rent_with_discount = 0
extra_discount = 0
final_price_per_ship_on_rent_with_all_discounts = 0
if season == "Spring":
    price_per_ship_on_rent = 3000
    if count_fishermen <= 6:
        discount = price_per_ship_on_rent * 0.10
        price_per_ship_on_rent_with_discount = price_per_ship_on_rent - discount
        if count_fishermen % 2 == 0:
            extra_discount = price_per_ship_on_rent_with_discount * 0.05
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount - extra_discount
        else:
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount
    elif count_fishermen <= 11:
        discount = price_per_ship_on_rent * 0.15
        price_per_ship_on_rent_with_discount = price_per_ship_on_rent - discount
        if count_fishermen % 2 == 0:
            extra_discount = price_per_ship_on_rent_with_discount * 0.05
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount - extra_discount
        else:
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount
    else:
        discount = price_per_ship_on_rent * 0.25
        price_per_ship_on_rent_with_discount = price_per_ship_on_rent - discount
        if count_fishermen % 2 == 0:
            extra_discount = price_per_ship_on_rent_with_discount * 0.05
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount - extra_discount
        else:
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount
elif season == "Summer":
    price_per_ship_on_rent = 4200
    if count_fishermen <= 6:
        discount = price_per_ship_on_rent * 0.10
        price_per_ship_on_rent_with_discount = price_per_ship_on_rent - discount
        if count_fishermen % 2 == 0:
            extra_discount = price_per_ship_on_rent_with_discount * 0.05
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount - extra_discount
        else:
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount
    elif count_fishermen <= 11:
        discount = price_per_ship_on_rent * 0.15
        price_per_ship_on_rent_with_discount = price_per_ship_on_rent - discount
        if count_fishermen % 2 == 0:
            extra_discount = price_per_ship_on_rent_with_discount * 0.05
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount - extra_discount
        else:
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount
    else:
        discount = price_per_ship_on_rent * 0.25
        price_per_ship_on_rent_with_discount = price_per_ship_on_rent - discount
        if count_fishermen % 2 == 0:
            extra_discount = price_per_ship_on_rent_with_discount * 0.05
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount - extra_discount
        else:
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount
elif season == "Autumn":
    price_per_ship_on_rent = 4200
    if count_fishermen <= 6:
        discount = price_per_ship_on_rent * 0.10
        final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent - discount
    elif count_fishermen <= 11:
        discount = price_per_ship_on_rent * 0.15
        final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent - discount
    else:
        discount = price_per_ship_on_rent * 0.25
        final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent - discount
elif season == "Winter":
    price_per_ship_on_rent = 2600
    if count_fishermen <= 6:
        discount = price_per_ship_on_rent * 0.10
        price_per_ship_on_rent_with_discount = price_per_ship_on_rent - discount
        if count_fishermen % 2 == 0:
            extra_discount = price_per_ship_on_rent_with_discount * 0.05
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount - extra_discount
        else:
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount
    elif count_fishermen <= 11:
        discount = price_per_ship_on_rent * 0.15
        price_per_ship_on_rent_with_discount = price_per_ship_on_rent - discount
        if count_fishermen % 2 == 0:
            extra_discount = price_per_ship_on_rent_with_discount * 0.05
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount - extra_discount
        else:
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount
    else:
        discount = price_per_ship_on_rent * 0.25
        price_per_ship_on_rent_with_discount = price_per_ship_on_rent - discount
        if count_fishermen % 2 == 0:
            extra_discount = price_per_ship_on_rent_with_discount * 0.05
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount - extra_discount
        else:
            final_price_per_ship_on_rent_with_all_discounts = price_per_ship_on_rent_with_discount
if group_budget >= final_price_per_ship_on_rent_with_all_discounts:
    money_left_over = abs(group_budget - final_price_per_ship_on_rent_with_all_discounts)
    print(f"Yes! You have {money_left_over:.2f} leva left.")
else:
    needed_more_money = abs(group_budget - final_price_per_ship_on_rent_with_all_discounts)
    print(f"Not enough money! You need {needed_more_money:.2f} leva.")
