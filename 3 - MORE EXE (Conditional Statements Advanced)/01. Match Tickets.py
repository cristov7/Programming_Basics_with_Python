budget = float(input())
category = input()
count_people_in_group = int(input())
price_per_transport = 0
if 1 <= count_people_in_group <= 4:
    price_per_transport = budget * 0.75
elif 5 <= count_people_in_group <= 9:
    price_per_transport = budget * 0.60
elif 10 <= count_people_in_group <= 24:
    price_per_transport = budget * 0.50
elif 25 <= count_people_in_group <= 49:
    price_per_transport = budget * 0.40
elif count_people_in_group >= 50:
    price_per_transport = budget * 0.25
left_money_from_transport = budget - price_per_transport
price_per_one_ticket = 0
price_per_all_tickets = 0
if category == "VIP":
    price_per_one_ticket = 499.99
    price_per_all_tickets = count_people_in_group * price_per_one_ticket
elif category == "Normal":
    price_per_one_ticket = 249.99
    price_per_all_tickets = count_people_in_group * price_per_one_ticket
all_expenses = price_per_transport + price_per_all_tickets
if budget >= all_expenses:
    money_left_over = abs(budget - all_expenses)
    print(f"Yes! You have {money_left_over:.2f} leva left.")
else:
    not_enough_money = abs(budget - all_expenses)
    print(f"Not enough money! You need {not_enough_money:.2f} leva.")
