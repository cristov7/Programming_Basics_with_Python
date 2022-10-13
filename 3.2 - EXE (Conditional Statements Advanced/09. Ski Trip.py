days_to_stay = int(input())
type_premises = input()
grade = input()
nights_in_the_premises = days_to_stay - 1
price_per_night_in_room_for_one_person = 18.00
price_per_night_in_apartment = 25.00
price_per_night_in_president_apartment = 35.0
price_per_all_nights = 0
discount = 0
price_per_all_nights_with_discount = 0
if type_premises == "room for one person":
    price_per_all_nights_with_discount = nights_in_the_premises * price_per_night_in_room_for_one_person
elif type_premises == "apartment":
    if days_to_stay < 10:
        price_per_all_nights = nights_in_the_premises * price_per_night_in_apartment
        discount = price_per_all_nights * 0.30
        price_per_all_nights_with_discount = price_per_all_nights - discount
    elif days_to_stay < 16:
        price_per_all_nights = nights_in_the_premises * price_per_night_in_apartment
        discount = price_per_all_nights * 0.35
        price_per_all_nights_with_discount = price_per_all_nights - discount
    else:
        price_per_all_nights = nights_in_the_premises * price_per_night_in_apartment
        discount = price_per_all_nights * 0.50
        price_per_all_nights_with_discount = price_per_all_nights - discount
elif type_premises == "president apartment":
    if days_to_stay < 10:
        price_per_all_nights = nights_in_the_premises * price_per_night_in_president_apartment
        discount = price_per_all_nights * 0.10
        price_per_all_nights_with_discount = price_per_all_nights - discount
    elif days_to_stay < 16:
        price_per_all_nights = nights_in_the_premises * price_per_night_in_president_apartment
        discount = price_per_all_nights * 0.15
        price_per_all_nights_with_discount = price_per_all_nights - discount
    else:
        price_per_all_nights = nights_in_the_premises * price_per_night_in_president_apartment
        discount = price_per_all_nights * 0.20
        price_per_all_nights_with_discount = price_per_all_nights - discount
grade_discount = 0
final_price_per_all_nights = 0
if grade == "positive":
    grade_discount = price_per_all_nights_with_discount * 0.25
    final_price_per_all_nights = price_per_all_nights_with_discount + grade_discount
elif grade == "negative":
    grade_discount = price_per_all_nights_with_discount * 0.10
    final_price_per_all_nights = price_per_all_nights_with_discount - grade_discount
print(f"{final_price_per_all_nights:.2f}")
