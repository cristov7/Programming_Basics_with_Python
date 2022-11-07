count_juniors_cyclist = int(input())
count_seniors_cyclist = int(input())
type_route = input()
count_all_participants = count_juniors_cyclist + count_seniors_cyclist
price_per_all_participants_in_juniors = 0
price_per_all_participants_in_seniors = 0
final_price_per_all_participants = 0
if type_route == "trail":
    price_per_one_participant_in_juniors = 5.50
    price_per_one_participant_in_seniors = 7
    price_per_all_participants_in_juniors = count_juniors_cyclist * price_per_one_participant_in_juniors
    price_per_all_participant_in_seniors = count_seniors_cyclist * price_per_one_participant_in_seniors
    final_price_per_all_participants = price_per_all_participants_in_juniors + price_per_all_participant_in_seniors
elif type_route == "cross-country":
    price_per_one_participant_in_juniors = 8
    price_per_one_participant_in_seniors = 9.50
    if count_all_participants >= 50:
        price_per_all_participants_in_juniors = count_juniors_cyclist * price_per_one_participant_in_juniors
        price_per_all_participant_in_seniors = count_seniors_cyclist * price_per_one_participant_in_seniors
        price_per_all_participants = price_per_all_participants_in_juniors + price_per_all_participant_in_seniors
        discount = price_per_all_participants * 0.25
        final_price_per_all_participants = price_per_all_participants - discount
    else:
        price_per_all_participants_in_juniors = count_juniors_cyclist * price_per_one_participant_in_juniors
        price_per_all_participant_in_seniors = count_seniors_cyclist * price_per_one_participant_in_seniors
        final_price_per_all_participants = price_per_all_participants_in_juniors + price_per_all_participant_in_seniors
elif type_route == "downhill":
    price_per_one_participant_in_juniors = 12.25
    price_per_one_participant_in_seniors = 13.75
    price_per_all_participants_in_juniors = count_juniors_cyclist * price_per_one_participant_in_juniors
    price_per_all_participant_in_seniors = count_seniors_cyclist * price_per_one_participant_in_seniors
    final_price_per_all_participants = price_per_all_participants_in_juniors + price_per_all_participant_in_seniors
elif type_route == "road":
    price_per_one_participant_in_juniors = 20
    price_per_one_participant_in_seniors = 21.50
    price_per_all_participants_in_juniors = count_juniors_cyclist * price_per_one_participant_in_juniors
    price_per_all_participant_in_seniors = count_seniors_cyclist * price_per_one_participant_in_seniors
    final_price_per_all_participants = price_per_all_participants_in_juniors + price_per_all_participant_in_seniors
expenses = final_price_per_all_participants * 0.05
money_per_donations = final_price_per_all_participants - expenses
print(f"{money_per_donations:.2f}")
