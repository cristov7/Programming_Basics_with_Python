count_months = int(input())
sum_price_per_electricity = 0
sum_price_per_water = 0
sum_price_per_internet = 0
sum_price_per_others = 0
sum_expenses = 0
for month in range(count_months):
    price_per_electricity = float(input())
    price_per_water = 20
    price_per_internet = 15
    price_per_others = (price_per_electricity + price_per_water + price_per_internet) * 1.20
    expenses = price_per_electricity + price_per_water + price_per_internet + price_per_others
    sum_price_per_electricity += price_per_electricity
    sum_price_per_water += price_per_water
    sum_price_per_internet += price_per_internet
    sum_price_per_others += price_per_others
    sum_expenses += expenses
average_expenses_per_one_month = sum_expenses / count_months
print(f"Electricity: {sum_price_per_electricity:.2f} lv")
print(f"Water: {sum_price_per_water:.2f} lv")
print(f"Internet: {sum_price_per_internet:.2f} lv")
print(f"Other: {sum_price_per_others:.2f} lv")
print(f"Average: {average_expenses_per_one_month:.2f} lv")
