square_meters = float(input())
price_per_one_square_meter = 7.61
full_price = price_per_one_square_meter * square_meters
discount = full_price * 0.18
final_price = full_price - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
