stage_of_championship = input()     # “Quarter final ” / “Semi final” / “Final”
type_ticket = input()               # “Standard” / “Premium” / “VIP”
count_tickets = int(input())
photo_with_the_trophy = input()     # "Y" / "N"
price_per_photo_with_the_trophy = 40
price_per_one_ticket = 0
if stage_of_championship == "Quarter final":
    if type_ticket == "Standard":
        price_per_one_ticket = 55.50
    elif type_ticket == "Premium":
        price_per_one_ticket = 105.20
    elif type_ticket == "VIP":
        price_per_one_ticket = 118.90
elif stage_of_championship == "Semi final":
    if type_ticket == "Standard":
        price_per_one_ticket = 75.88
    elif type_ticket == "Premium":
        price_per_one_ticket = 125.22
    elif type_ticket == "VIP":
        price_per_one_ticket = 300.40
elif stage_of_championship == "Final":
    if type_ticket == "Standard":
        price_per_one_ticket = 110.10
    elif type_ticket == "Premium":
        price_per_one_ticket = 160.66
    elif type_ticket == "VIP":
        price_per_one_ticket = 400
total_price_per_tickets = price_per_one_ticket * count_tickets
if total_price_per_tickets > 4000:
    discount = total_price_per_tickets * 0.25
    total_price_per_tickets -= discount
elif total_price_per_tickets > 2500:
    discount = total_price_per_tickets * 0.10
    total_price_per_tickets -= discount
    if photo_with_the_trophy == "Y":
        price_per_photo = price_per_photo_with_the_trophy * count_tickets
        total_price_per_tickets += price_per_photo
else:
    if photo_with_the_trophy == "Y":
        price_per_photo = price_per_photo_with_the_trophy * count_tickets
        total_price_per_tickets += price_per_photo
print(f"{total_price_per_tickets:.2f}")
