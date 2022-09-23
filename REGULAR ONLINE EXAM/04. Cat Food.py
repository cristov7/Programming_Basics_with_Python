count_group_cats_1 = 0
count_group_cats_2 = 0
count_group_cats_3 = 0
total_cat_food_in_grams = 0
count_cats = int(input())
for cat in range(count_cats):
    cat_food_in_grams = float(input())
    total_cat_food_in_grams += cat_food_in_grams
    if 100 <= cat_food_in_grams < 200:
        count_group_cats_1 += 1
    elif 200 <= cat_food_in_grams < 300:
        count_group_cats_2 += 1
    elif 300 <= cat_food_in_grams < 400:
        count_group_cats_3 += 1
total_cat_food_in_kg = total_cat_food_in_grams / 1000
one_kg_cat_food = 12.45
price_for_cat_food_in_one_day = total_cat_food_in_kg * one_kg_cat_food
print(f"Group 1: {count_group_cats_1} cats.")
print(f"Group 2: {count_group_cats_2} cats.")
print(f"Group 3: {count_group_cats_3} cats.")
print(f"Price for food per day: {price_for_cat_food_in_one_day:.2f} lv.")
