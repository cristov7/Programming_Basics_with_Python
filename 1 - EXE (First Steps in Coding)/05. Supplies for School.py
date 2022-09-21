count_packages_with_pens = int(input())
count_packages_with_markers = int(input())
liters_preparation_for_cleaning = int(input())
discount_in_percents = int(input()) / 100
one_package_with_pens = 5.80
one_package_with_markers = 7.20
one_liter_preparation_for_cleaning = 1.20
full_price_per_pens = count_packages_with_pens * one_package_with_pens
full_price_per_markers = count_packages_with_markers * one_package_with_markers
full_price_per_preparation_for_cleaning = liters_preparation_for_cleaning * one_liter_preparation_for_cleaning
full_price = full_price_per_pens + full_price_per_markers + full_price_per_preparation_for_cleaning
discount = full_price * discount_in_percents
final_price = full_price - discount
print(final_price)
