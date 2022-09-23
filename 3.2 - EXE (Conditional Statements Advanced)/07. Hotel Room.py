month = input()
count_nights = int(input())
price_per_one_night_in_apartment = 0
price_per_one_night_in_studio = 0
discount_per_apartment = 0
discount_per_studio = 0
if month == "May" or month == "October":
    price_per_one_night_in_apartment = 65
    price_per_one_night_in_studio = 50
    if count_nights > 14:
        discount_per_apartment = price_per_one_night_in_apartment * 0.10
        price_per_one_night_in_apartment -= discount_per_apartment
        discount_per_studio = price_per_one_night_in_studio * 0.30
        price_per_one_night_in_studio -= discount_per_studio
    elif count_nights > 7:
        discount_per_studio = price_per_one_night_in_studio * 0.05
        price_per_one_night_in_studio -= discount_per_studio
elif month == "June" or month == "September":
    price_per_one_night_in_apartment = 68.70
    price_per_one_night_in_studio = 75.20
    if count_nights > 14:
        discount_per_apartment = price_per_one_night_in_apartment * 0.10
        price_per_one_night_in_apartment -= discount_per_apartment
        discount_per_studio = price_per_one_night_in_studio * 0.20
        price_per_one_night_in_studio -= discount_per_studio
elif month == "July" or month == "August":
    price_per_one_night_in_apartment = 77
    price_per_one_night_in_studio = 76
    if count_nights > 14:
        discount_per_apartment = price_per_one_night_in_apartment * 0.10
        price_per_one_night_in_apartment -= discount_per_apartment
full_price_per_apartment = count_nights * price_per_one_night_in_apartment
full_price_per_studio = count_nights * price_per_one_night_in_studio
print(f"Apartment: {full_price_per_apartment:.2f} lv.")
print(f"Studio: {full_price_per_studio:.2f} lv.")
