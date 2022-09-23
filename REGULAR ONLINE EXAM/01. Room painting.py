from math import ceil
from math import floor
count_paint_boxes = int(input())
count_rolls_of_wallpapers = int(input())
price_per_one_pair_gloves = float(input())
price_per_one_bush = float(input())
price_per_one_paint_box = 21.50
price_per_one_roll_of_wallpaper = 5.20
count_gloves = ceil(count_rolls_of_wallpapers * 0.35)
count_bushes = floor(count_paint_boxes * 0.48)
final_price_per_paint_boxes = count_paint_boxes * price_per_one_paint_box
final_price_per_rolls_of_wallpapers = count_rolls_of_wallpapers * price_per_one_roll_of_wallpaper
final_price_per_gloves = count_gloves * price_per_one_pair_gloves
final_price_per_bushes = count_bushes * price_per_one_bush
sum_price = final_price_per_paint_boxes + final_price_per_rolls_of_wallpapers + final_price_per_gloves + final_price_per_bushes
delivery = sum_price / 15
print(f"This delivery will cost {delivery:.2f} lv.")
