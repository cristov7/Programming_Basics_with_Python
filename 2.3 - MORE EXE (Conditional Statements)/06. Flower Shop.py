from math import floor
from math import ceil
count_magnolias = int(input())
count_hyacinths = int(input())
count_roses = int(input())
count_cactus = int(input())
price_per_gift = float(input())
price_per_one_magnolia = 3.25
price_per_one_hyacinths = 4
price_per_one_rose = 3.50
price_per_one_cactus = 8
full_price_per_magnolias = count_magnolias * price_per_one_magnolia
full_price_per_hyacinths = count_hyacinths * price_per_one_hyacinths
full_price_per_roses = count_roses * price_per_one_rose
full_price_per_cactus = count_cactus * price_per_one_cactus
full_price_per_flowers = full_price_per_magnolias + full_price_per_hyacinths + full_price_per_roses + full_price_per_cactus
taxes = full_price_per_flowers * 0.05
final_sum = full_price_per_flowers - taxes
if final_sum >= price_per_gift:
    money_left_over = abs(final_sum - price_per_gift)
    print(f"She is left with {floor(money_left_over)} leva.")
else:
    needed_more_money = abs(final_sum - price_per_gift)
    print(f"She will have to borrow {ceil(needed_more_money)} leva.")
