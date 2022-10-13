budget = float(input())
the_season_is_summer_or_winter = input()
destination = ""
camp_or_hotel = ""
expenses = 0
if budget <= 100:
    destination = "Bulgaria"
    if the_season_is_summer_or_winter == "summer":
        camp_or_hotel = "Camp"
        expenses = budget * 0.30
    elif the_season_is_summer_or_winter == "winter":
        camp_or_hotel = "Hotel"
        expenses = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if the_season_is_summer_or_winter == "summer":
        camp_or_hotel = "Camp"
        expenses = budget * 0.40
    elif the_season_is_summer_or_winter == "winter":
        camp_or_hotel = "Hotel"
        expenses = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    camp_or_hotel = "Hotel"
    expenses = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{camp_or_hotel} - {expenses:.2f}")
