count_km = int(input())
time_of_the_travel_is_day_or_night = input()
the_cheapest_price = 0
price_by_taxi = 0
starting_tax = 0.70
if time_of_the_travel_is_day_or_night == "day":
    price_per_one_km = 0.79
    price_by_taxi = starting_tax + (count_km * price_per_one_km)
    the_cheapest_price = price_by_taxi
elif time_of_the_travel_is_day_or_night == "night":
    price_per_one_km = 0.90
    price_by_taxi = starting_tax + (count_km * price_per_one_km)
    the_cheapest_price = price_by_taxi
price_by_bus = 0
if count_km >= 20:
    price_per_one_km = 0.09
    price_by_bus = count_km * price_per_one_km
    if price_by_bus < the_cheapest_price:
        the_cheapest_price = price_by_bus
price_by_train = 0
if count_km >= 100:
    price_per_one_km = 0.06
    price_by_train = count_km * price_per_one_km
    if price_by_train < the_cheapest_price:
        the_cheapest_price = price_by_train
print(f"{the_cheapest_price:.2f}")
