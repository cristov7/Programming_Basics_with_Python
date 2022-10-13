count_purchased_chrysanthemums = int(input())
count_purchased_roses = int(input())
count_purchased_tulips = int(input())
season = input()
holiday = input()
count_all_purchased_flowers = count_purchased_chrysanthemums + count_purchased_roses + count_purchased_tulips
arranging = 2
price_per_one_chrysanthemum = 0
price_per_one_rose = 0
price_per_one_tulip = 0
price_per_all_chrysanthemums = 0
price_per_all_roses = 0
price_per_all_tulips = 0
price_per_all_flowers_without_arranging = 0
final_price = 0
if season == "Spring":
    if holiday == "N":
        price_per_one_chrysanthemum = 2
        price_per_one_rose = 4.10
        price_per_one_tulip = 2.50
        price_per_all_chrysanthemums = count_purchased_chrysanthemums * price_per_one_chrysanthemum
        price_per_all_roses = count_purchased_roses * price_per_one_rose
        price_per_all_tulips = count_purchased_tulips * price_per_one_tulip
        price_per_all_flowers_without_arranging = price_per_all_chrysanthemums + price_per_all_roses + price_per_all_tulips
        if count_purchased_tulips > 7:
            discount = price_per_all_flowers_without_arranging * 0.05
            price_per_all_flowers_without_arranging -= discount
    elif holiday == "Y":
        expensive_price = 1.15
        price_per_one_chrysanthemum = 2 * expensive_price
        price_per_one_rose = 4.10 * expensive_price
        price_per_one_tulip = 2.50 * expensive_price
        price_per_all_chrysanthemums = count_purchased_chrysanthemums * price_per_one_chrysanthemum
        price_per_all_roses = count_purchased_roses * price_per_one_rose
        price_per_all_tulips = count_purchased_tulips * price_per_one_tulip
        price_per_all_flowers_without_arranging = price_per_all_chrysanthemums + price_per_all_roses + price_per_all_tulips
        if count_purchased_tulips > 7:
            discount = price_per_all_flowers_without_arranging * 0.05
            price_per_all_flowers_without_arranging -= discount
elif season == "Summer":
    if holiday == "N":
        price_per_one_chrysanthemum = 2
        price_per_one_rose = 4.10
        price_per_one_tulip = 2.50
        price_per_all_chrysanthemums = count_purchased_chrysanthemums * price_per_one_chrysanthemum
        price_per_all_roses = count_purchased_roses * price_per_one_rose
        price_per_all_tulips = count_purchased_tulips * price_per_one_tulip
        price_per_all_flowers_without_arranging = price_per_all_chrysanthemums + price_per_all_roses + price_per_all_tulips
    elif holiday == "Y":
        expensive_price = 1.15
        price_per_one_chrysanthemum = 2 * expensive_price
        price_per_one_rose = 4.10 * expensive_price
        price_per_one_tulip = 2.50 * expensive_price
        price_per_all_chrysanthemums = count_purchased_chrysanthemums * price_per_one_chrysanthemum
        price_per_all_roses = count_purchased_roses * price_per_one_rose
        price_per_all_tulips = count_purchased_tulips * price_per_one_tulip
        price_per_all_flowers_without_arranging = price_per_all_chrysanthemums + price_per_all_roses + price_per_all_tulips
elif season == "Autumn":
    if holiday == "N":
        price_per_one_chrysanthemum = 3.75
        price_per_one_rose = 4.50
        price_per_one_tulip = 4.15
        price_per_all_chrysanthemums = count_purchased_chrysanthemums * price_per_one_chrysanthemum
        price_per_all_roses = count_purchased_roses * price_per_one_rose
        price_per_all_tulips = count_purchased_tulips * price_per_one_tulip
        price_per_all_flowers_without_arranging = price_per_all_chrysanthemums + price_per_all_roses + price_per_all_tulips
    elif holiday == "Y":
        expensive_price = 1.15
        price_per_one_chrysanthemum = 3.75 * expensive_price
        price_per_one_rose = 4.50 * expensive_price
        price_per_one_tulip = 4.15 * expensive_price
        price_per_all_chrysanthemums = count_purchased_chrysanthemums * price_per_one_chrysanthemum
        price_per_all_roses = count_purchased_roses * price_per_one_rose
        price_per_all_tulips = count_purchased_tulips * price_per_one_tulip
        price_per_all_flowers_without_arranging = price_per_all_chrysanthemums + price_per_all_roses + price_per_all_tulips
elif season == "Winter":
    if holiday == "N":
        price_per_one_chrysanthemum = 3.75
        price_per_one_rose = 4.50
        price_per_one_tulip = 4.15
        price_per_all_chrysanthemums = count_purchased_chrysanthemums * price_per_one_chrysanthemum
        price_per_all_roses = count_purchased_roses * price_per_one_rose
        price_per_all_tulips = count_purchased_tulips * price_per_one_tulip
        price_per_all_flowers_without_arranging = price_per_all_chrysanthemums + price_per_all_roses + price_per_all_tulips
        if count_purchased_roses >= 10:
            discount = price_per_all_flowers_without_arranging * 0.10
            price_per_all_flowers_without_arranging -= discount
    elif holiday == "Y":
        expensive_price = 1.15
        price_per_one_chrysanthemum = 3.75 * expensive_price
        price_per_one_rose = 4.50 * expensive_price
        price_per_one_tulip = 4.15 * expensive_price
        price_per_all_chrysanthemums = count_purchased_chrysanthemums * price_per_one_chrysanthemum
        price_per_all_roses = count_purchased_roses * price_per_one_rose
        price_per_all_tulips = count_purchased_tulips * price_per_one_tulip
        price_per_all_flowers_without_arranging = price_per_all_chrysanthemums + price_per_all_roses + price_per_all_tulips
        if count_purchased_roses >= 10:
            discount = price_per_all_flowers_without_arranging * 0.10
            price_per_all_flowers_without_arranging -= discount
if count_all_purchased_flowers > 20:
    discount = price_per_all_flowers_without_arranging * 0.20
    price_per_all_flowers_without_arranging -= discount
    final_price = price_per_all_flowers_without_arranging + arranging
else:
    final_price = price_per_all_flowers_without_arranging + arranging
print(f"{final_price:.2f}")
