type_of_fuel = input()
liters_of_fuel_in_the_tank = float(input())
if type_of_fuel == "Diesel" or type_of_fuel == "Gasoline" or type_of_fuel == "Gas":
    if liters_of_fuel_in_the_tank >= 25:
        print(f"You have enough {type_of_fuel.lower()}.")
    else:
        print(f"Fill your tank with {type_of_fuel.lower()}!")
else:
    print("Invalid fuel!")
