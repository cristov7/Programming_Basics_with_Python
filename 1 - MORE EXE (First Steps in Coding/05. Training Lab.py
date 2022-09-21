hall_length_in_meters = float(input())
hall_width_in_meters = float(input())
S_hall = hall_length_in_meters * hall_width_in_meters
one_work_place_length_in_meters = 1.20
one_work_place_width_in_meters = 0.70
S_one_work_place = one_work_place_length_in_meters * one_work_place_width_in_meters
corridor_length_in_meters = hall_length_in_meters
corridor_width_in_meters = 1
S_corridor = hall_length_in_meters * corridor_width_in_meters
S_door = S_one_work_place
S_department = 2 * S_one_work_place
work_places_row = (hall_width_in_meters - corridor_width_in_meters) // 0.70
work_places_column = hall_length_in_meters // 1.20
possible_work_places = (work_places_row * work_places_column) - (S_door + S_department)
print(int(possible_work_places))
