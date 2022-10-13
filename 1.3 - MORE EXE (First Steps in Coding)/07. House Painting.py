house_x = float(input())
house_y = float(input())
house_h = float(input())
# walls => green paint
# roof => red paint
one_liter_green_paint_in_square_meters = 3.4
one_liter_red_paint_in_square_meters = 4.3
door_x = 1.2
door_y = 2
S_door = door_x * door_y
S_front_wall = (house_x * house_x) - S_door
S_rear_wall = house_x * house_x
window_x = 1.5
window_y = 1.5
S_window = window_x * window_y
S_lateral_walls = 2 * ((house_x * house_y) - S_window)
square_meters_per_green_paint = S_front_wall + S_rear_wall + S_lateral_walls
green_paint_needed_liters = square_meters_per_green_paint / one_liter_green_paint_in_square_meters
print(f"{green_paint_needed_liters:.2f}")
S_front_roof = (house_x * house_h) / 2
S_rear_roof = (house_x * house_h) / 2
S_lateral_roofs = 2 * (house_x * house_y)
square_meters_per_red_paint = S_front_roof + S_rear_roof + S_lateral_roofs
red_paint_needed_liters = square_meters_per_red_paint / one_liter_red_paint_in_square_meters
print(f"{red_paint_needed_liters:.2f}")
