money_inherited = float(input())
years_to_live = int(input())
current_age = 18
money_left_over = money_inherited
for year in range(1800, years_to_live + 1):
    if year % 2 != 0:   # even_year
        expenses = 12000 + (50 * current_age)
        money_left_over -= expenses
        current_age += 1
    else:               # odd_year
        expenses = 12000
        money_left_over -= expenses
        current_age += 1
if money_left_over >= 0:
    print(f"Yes! He will live a carefree life and will have {money_left_over:.2f} dollars left.")
else:
    not_enough_money = abs(money_left_over)
    print(f"He will need {not_enough_money:.2f} dollars to survive.")
