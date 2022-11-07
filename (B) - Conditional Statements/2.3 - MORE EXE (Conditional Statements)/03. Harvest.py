from math import floor
from math import ceil
square_meters_vineyard = int(input())
grapes_per_one_square_meter_in_kg = float(input())
needed_liters_wine_to_sell = int(input())
count_workers = int(input())
harvest_to_wine_in_square_meters = square_meters_vineyard * 0.40
one_liter_wine_in_kg = 2.5
grapes_in_kg = harvest_to_wine_in_square_meters * grapes_per_one_square_meter_in_kg
total_wine_in_liters = grapes_in_kg / one_liter_wine_in_kg
if total_wine_in_liters < needed_liters_wine_to_sell:
    needed_more_wine = abs(total_wine_in_liters - needed_liters_wine_to_sell)
    print(f"It will be a tough winter! More {floor(needed_more_wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(total_wine_in_liters)} liters.")
    left_wine_in_liters = abs(total_wine_in_liters - needed_liters_wine_to_sell)
    wine_per_one_worker = left_wine_in_liters / count_workers
    print(f"{ceil(left_wine_in_liters)} liters left -> {ceil(wine_per_one_worker)} liters per person.")
