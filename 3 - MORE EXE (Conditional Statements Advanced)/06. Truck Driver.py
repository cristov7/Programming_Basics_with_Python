season = input()
km_per_month = float(input())
one_season_in_months = 4
price_per_one_km = 0
if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
        price_per_one_km = 0.75
    elif 5000 < km_per_month <= 10000:
        price_per_one_km = 0.95
    elif 10000 < km_per_month <= 20000:
        price_per_one_km = 1.45
elif season == "Summer":
    if km_per_month <= 5000:
        price_per_one_km = 0.90
    elif 5000 < km_per_month <= 10000:
        price_per_one_km = 1.10
    elif 10000 < km_per_month <= 20000:
        price_per_one_km = 1.45
elif season == "Winter":
    if km_per_month <= 5000:
        price_per_one_km = 1.05
    elif 5000 < km_per_month <= 10000:
        price_per_one_km = 1.25
    elif 10000 < km_per_month <= 20000:
        price_per_one_km = 1.45
profit_per_month_without_taxes = price_per_one_km * km_per_month
profit_per_season_without_taxes = profit_per_month_without_taxes * one_season_in_months
taxes = profit_per_season_without_taxes * 0.10
final_salary = profit_per_season_without_taxes - taxes
print(f"{final_salary:.2f}")
