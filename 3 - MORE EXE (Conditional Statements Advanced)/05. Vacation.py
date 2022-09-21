budget = float(input())
season = input()
location = ""
premises = ""
price_per_vacation = 0
if budget <= 1000:
    premises = "Camp"
    if season == "Summer":
        location = "Alaska"
        price_per_vacation = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price_per_vacation = budget * 0.45
elif 1000 < budget <= 3000:
    premises = "Hut"
    if season == "Summer":
        location = "Alaska"
        price_per_vacation = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price_per_vacation = budget * 0.60
else:
    premises = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price_per_vacation = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        price_per_vacation = budget * 0.90
print(f"{location} - {premises} - {price_per_vacation:.2f}")
