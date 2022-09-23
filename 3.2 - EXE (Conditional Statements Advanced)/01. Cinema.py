type_of_projection = input()
rows = int(input())
columns = int(input())
full_places = rows * columns
income_from_all_tickets = 0
if type_of_projection == "Premiere":
    price_per_ticket = 12.00
    income_from_all_tickets = full_places * price_per_ticket
elif type_of_projection == "Normal":
    price_per_ticket = 7.50
    income_from_all_tickets = full_places * price_per_ticket
elif type_of_projection == "Discount":
    price_per_ticket = 5.00
    income_from_all_tickets = full_places * price_per_ticket
print(f"{income_from_all_tickets:.2f} leva")
