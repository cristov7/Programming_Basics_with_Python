count_bottles_of_detergent = int(input())
one_bottle_of_detergent_in_ml = 750
total_detergents_in_ml = count_bottles_of_detergent * one_bottle_of_detergent_in_ml
washing_one_plate_in_ml = 5
washing_one_pot_in_ml = 15
counter = 0
count_clean_plates = 0
count_clean_pots = 0
while True:
    command = input()
    if command == "End":
        print("Detergent was enough!")
        print(f"{count_clean_plates} dishes and {count_clean_pots} pots were washed.")
        print(f"Leftover detergent {total_detergents_in_ml} ml.")
        break
    else:
        counter += 1
        if counter % 3 == 0:
            count_dishes_per_washing_in_ml = int(command) * washing_one_pot_in_ml
            total_detergents_in_ml -= count_dishes_per_washing_in_ml
            if total_detergents_in_ml >= 0:
                count_clean_pots += int(command)
                continue
            else:
                needed_more_detergent_in_ml = abs(total_detergents_in_ml)
                print(f"Not enough detergent, {needed_more_detergent_in_ml} ml. more necessary!")
                break
        else:
            count_dishes_per_washing_in_ml = int(command) * washing_one_plate_in_ml
            total_detergents_in_ml -= count_dishes_per_washing_in_ml
            if total_detergents_in_ml >= 0:
                count_clean_plates += int(command)
                continue
            else:
                needed_more_detergent_in_ml = abs(total_detergents_in_ml)
                print(f"Not enough detergent, {needed_more_detergent_in_ml} ml. more necessary!")
                break
