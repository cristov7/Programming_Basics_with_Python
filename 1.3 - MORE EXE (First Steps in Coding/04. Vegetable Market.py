price_per_one_kg_vegetables_in_lv = float(input())
price_per_one_kg_fruits_in_lv = float(input())
available_kgs_vegetables = int(input())
available_kgs_fruits = int(input())
earn_money_in_lv_per_vegetables = available_kgs_vegetables * price_per_one_kg_vegetables_in_lv
earn_money_in_lv_per_fruits = available_kgs_fruits * price_per_one_kg_fruits_in_lv
full_earn_money_in_lv = earn_money_in_lv_per_vegetables + earn_money_in_lv_per_fruits
full_earn_money_in_euro = full_earn_money_in_lv / 1.94
print(f"{full_earn_money_in_euro:.2f}")
