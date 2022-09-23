price_per_one_toy = 5
price_per_gifts_juniors = 0
count_people_under_and_16_years_old = 0
price_per_one_sweater = 15
price_per_gifts_seniors = 0
count_people_over_16_years_old = 0
while True:
    command = input()
    if command == "Christmas":
        print(f"Number of adults: {count_people_over_16_years_old}")
        print(f"Number of kids: {count_people_under_and_16_years_old}")
        print(f"Money for toys: {price_per_gifts_juniors}")
        print(f"Money for sweaters: {price_per_gifts_seniors}")
        break
    else:
        age = int(command)
        if age <= 16:
            count_people_under_and_16_years_old += 1
            price_per_gifts_juniors += price_per_one_toy
        else:
            count_people_over_16_years_old += 1
            price_per_gifts_seniors += price_per_one_sweater
