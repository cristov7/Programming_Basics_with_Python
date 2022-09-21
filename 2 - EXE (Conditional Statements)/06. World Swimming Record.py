from math import floor
the_record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_one_meter_distance = float(input())
water_resistance_per_every_15_meters_in_seconds = 12.5
time_per_distance_in_seconds_without_water_resistance = distance_in_meters * time_in_seconds_per_one_meter_distance
time_per_water_resistance_in_seconds = (floor(distance_in_meters / 15)) * 12.5
full_time_per_distance_in_seconds = time_per_distance_in_seconds_without_water_resistance + time_per_water_resistance_in_seconds
if full_time_per_distance_in_seconds < the_record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {full_time_per_distance_in_seconds:.2f} seconds.")
else:
    more_time_in_seconds = abs(full_time_per_distance_in_seconds - the_record_in_seconds)
    print(f"No, he failed! He was {more_time_in_seconds:.2f} seconds slower.")
