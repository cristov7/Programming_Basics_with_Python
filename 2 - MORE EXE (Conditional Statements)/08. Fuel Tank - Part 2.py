type_of_fuel = input()
amount_of_fuel = float(input())
do_you_have_a_club_card = input()
price_per_one_liter_gasoline = 2.22
price_per_one_liter_diesel = 2.33
price_per_one_liter_gas = 0.93
if do_you_have_a_club_card == "Yes":
    price_per_one_liter_gasoline = 2.22 - 0.18
    price_per_one_liter_diesel = 2.33 - 0.12
    price_per_one_liter_gas = 0.93 - 0.08
final_price_per_fuel = 0
discount = 0
if 20 <= amount_of_fuel <= 25:
    if type_of_fuel == "Gas":
        price_per_fuel = amount_of_fuel * price_per_one_liter_gas
        discount = price_per_fuel * 0.08
        final_price_per_fuel = price_per_fuel - discount
    elif type_of_fuel == "Gasoline":
        price_per_fuel = amount_of_fuel * price_per_one_liter_gasoline
        discount = price_per_fuel * 0.08
        final_price_per_fuel = price_per_fuel - discount
    elif type_of_fuel == "Diesel":
        price_per_fuel = amount_of_fuel * price_per_one_liter_diesel
        discount = price_per_fuel * 0.08
        final_price_per_fuel = price_per_fuel - discount
elif amount_of_fuel > 25:
    if type_of_fuel == "Gas":
        price_per_fuel = amount_of_fuel * price_per_one_liter_gas
        discount = price_per_fuel * 0.10
        final_price_per_fuel = price_per_fuel - discount
    elif type_of_fuel == "Gasoline":
        price_per_fuel = amount_of_fuel * price_per_one_liter_gasoline
        discount = price_per_fuel * 0.10
        final_price_per_fuel = price_per_fuel - discount
    elif type_of_fuel == "Diesel":
        price_per_fuel = amount_of_fuel * price_per_one_liter_diesel
        discount = price_per_fuel * 0.10
        final_price_per_fuel = price_per_fuel - discount
else:
    if type_of_fuel == "Gas":
        final_price_per_fuel = amount_of_fuel * price_per_one_liter_gas
    elif type_of_fuel == "Gasoline":
        final_price_per_fuel = amount_of_fuel * price_per_one_liter_gasoline
    elif type_of_fuel == "Diesel":
        final_price_per_fuel = amount_of_fuel * price_per_one_liter_diesel
print(f"{final_price_per_fuel:.2f} lv.")
