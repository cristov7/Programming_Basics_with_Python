taxes_per_one_year_for_basketball = int(input())
basketball_shoes = taxes_per_one_year_for_basketball * 0.60
basketball_equipment = basketball_shoes * 0.80
basketball_ball = basketball_equipment * 0.25
basketball_accessories = basketball_ball * 0.20
full_expenses = taxes_per_one_year_for_basketball + basketball_shoes + basketball_equipment + basketball_ball + basketball_accessories
print(full_expenses)
