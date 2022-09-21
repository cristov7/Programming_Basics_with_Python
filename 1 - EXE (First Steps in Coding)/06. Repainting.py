needed_quantity_nylon_in_square_meters = int(input()) + 2
needed_quantity_paint_in_liters = int(input()) * 1.10
needed_quantity_thinner_in_liters = int(input())
needed_hours_to_work = int(input())
nylon_per_one_square_meter = 1.50
paint_per_one_liter = 14.50
thinner_per_one_liter = 5.00
bags = 0.40
price_per_nylons = needed_quantity_nylon_in_square_meters * nylon_per_one_square_meter
price_per_paint = needed_quantity_paint_in_liters * paint_per_one_liter
price_per_thinner = needed_quantity_thinner_in_liters * thinner_per_one_liter
expenses_per_materials = bags + price_per_nylons + price_per_paint + price_per_thinner
price_per_one_hour_work = expenses_per_materials * 0.30
expenses_per_work = needed_hours_to_work * price_per_one_hour_work
final_price = expenses_per_materials + expenses_per_work
print(final_price)
