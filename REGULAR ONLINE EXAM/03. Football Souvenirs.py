team = input()                          # "Argentina", "Brazil", "Croatia", "Denmark"
type_souvenir = input()                 # "flags", "caps", "posters", "stickers"
count_bought_souvenirs = int(input())
price_per_souvenir = 0
total_price = 0
if team == "Argentina":
    if type_souvenir == "flags":
        price_per_souvenir = 3.25
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    elif type_souvenir == "caps":
        price_per_souvenir = 7.20
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    elif type_souvenir == "posters":
        price_per_souvenir = 5.10
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    elif type_souvenir == "stickers":
        price_per_souvenir = 1.25
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    else:
        print("Invalid stock!")
elif team == "Brazil":
    if type_souvenir == "flags":
        price_per_souvenir = 4.20
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    elif type_souvenir == "caps":
        price_per_souvenir = 8.50
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    elif type_souvenir == "posters":
        price_per_souvenir = 5.35
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    elif type_souvenir == "stickers":
        price_per_souvenir = 1.20
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    else:
        print("Invalid stock!")
elif team == "Croatia":
    if type_souvenir == "flags":
        price_per_souvenir = 2.75
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    elif type_souvenir == "caps":
        price_per_souvenir = 6.90
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    elif type_souvenir == "posters":
        price_per_souvenir = 4.95
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    elif type_souvenir == "stickers":
        price_per_souvenir = 1.10
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    else:
        print("Invalid stock!")
elif team == "Denmark":
    if type_souvenir == "flags":
        price_per_souvenir = 3.10
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    elif type_souvenir == "caps":
        price_per_souvenir = 6.50
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    elif type_souvenir == "posters":
        price_per_souvenir = 4.80
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    elif type_souvenir == "stickers":
        price_per_souvenir = 0.90
        total_price = price_per_souvenir * count_bought_souvenirs
        print(f"Pepi bought {count_bought_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")
    else:
        print("Invalid stock!")
else:
    print("Invalid country!")
