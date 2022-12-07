days_to_stay = int(input())     # пример: 11 дни = 10 нощувки
type_premises = input()         # "room for one person" / "apartment" / "president apartment"
degree = input()                # "positive"  / "negative"
nights = days_to_stay - 1
price_per_night = 0
discount = 0
price_per_all_nights = 0
if type_premises == "room for one person":
    price_per_night = 18
    price_per_all_nights = nights * price_per_night
elif type_premises == "apartment":
    price_per_night = 25
    if days_to_stay < 10:
        discount = 0.70
        price_per_all_nights = (nights * price_per_night) * discount
    elif days_to_stay <= 15:
        discount = 0.65
        price_per_all_nights = (nights * price_per_night) * discount
    else:
        discount = 0.50
        price_per_all_nights = (nights * price_per_night) * discount
elif type_premises == "president apartment":
    price_per_night = 35
    if days_to_stay < 10:
        discount = 0.90
        price_per_all_nights = (nights * price_per_night) * discount
    elif days_to_stay <= 15:
        discount = 0.85
        price_per_all_nights = (nights * price_per_night) * discount
    else:
        discount = 0.80
        price_per_all_nights = (nights * price_per_night) * discount
if degree == "positive":
    extra_taxes = 1.25
    price_per_all_nights *= extra_taxes
elif degree == "negative":
    more_discount = 0.90
    price_per_all_nights *= more_discount
print(f"{price_per_all_nights:.2f}")
