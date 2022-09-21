count_chicken_menus = int(input())
count_fish_menus = int(input())
count_vegetarian_menus = int(input())
price_per_one_chicken_menu = 10.35
price_per_one_fish_menu = 12.40
price_per_one_vegetarian_menu = 8.15
full_price_per_chicken_menus = count_chicken_menus * price_per_one_chicken_menu
full_price_per_fish_menus = count_fish_menus * price_per_one_fish_menu
full_price_per_vegetarian_menus = count_vegetarian_menus * price_per_one_vegetarian_menu
full_price_per_all_menus = full_price_per_chicken_menus + full_price_per_fish_menus + full_price_per_vegetarian_menus
dessert = full_price_per_all_menus * 0.20
delivery = 2.50
final_price = full_price_per_all_menus + dessert + delivery
print(final_price)
