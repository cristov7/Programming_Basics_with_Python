day_of_the_week = input()
price_per_ticket = 0
if day_of_the_week == "Monday"\
        or day_of_the_week == "Tuesday"\
        or day_of_the_week == "Friday":
    price_per_ticket = 12
elif day_of_the_week == "Wednesday"\
        or day_of_the_week == "Thursday":
    price_per_ticket = 14
elif day_of_the_week == "Saturday"\
        or day_of_the_week == "Sunday":
    price_per_ticket = 16
print(price_per_ticket)
