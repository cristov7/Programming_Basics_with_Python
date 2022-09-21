from math import floor
from math import ceil
count_days = int(input())
left_food_in_kg = int(input())
food_per_day_for_dog_in_kg = float(input())
food_per_day_for_cat_in_kg = float(input())
food_per_day_for_turtle_in_grams = float(input())
eating_food_by_dog_in_kg = count_days * food_per_day_for_dog_in_kg
eating_food_by_cat_in_kg = count_days * food_per_day_for_cat_in_kg
eating_food_by_turtle_in_kg = count_days * (food_per_day_for_turtle_in_grams / 1000)
eating_food_by_all_in_kg = eating_food_by_dog_in_kg + eating_food_by_cat_in_kg + eating_food_by_turtle_in_kg
if left_food_in_kg >= eating_food_by_all_in_kg:
    left_more_food_in_kg = abs(left_food_in_kg - eating_food_by_all_in_kg)
    print(f"{floor(left_more_food_in_kg)} kilos of food left.")
else:
    needed_more_food_in_kg = abs(left_food_in_kg - eating_food_by_all_in_kg)
    print(f"{ceil(needed_more_food_in_kg)} more kilos of food are needed.")
