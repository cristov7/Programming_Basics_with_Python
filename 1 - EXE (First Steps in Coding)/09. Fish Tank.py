length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percent_taken_place = float(input())
percent_free_space = (100 - percent_taken_place) / 100
full_place_in_cubic_cm = length_in_cm * width_in_cm * height_in_cm
needed_liters_in_cubic_cm = full_place_in_cubic_cm * percent_free_space
needed_liters_in_cm = needed_liters_in_cubic_cm / 1000
print(needed_liters_in_cm)
