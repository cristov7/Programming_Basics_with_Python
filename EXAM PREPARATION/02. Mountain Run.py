from math import floor
record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_sec_per_one_meter = float(input())
delay = ((distance_in_meters // 50) * 30)
current_time_in_sec = (time_in_sec_per_one_meter * distance_in_meters) + floor(delay)
if current_time_in_sec < record_in_seconds:
    print(f"Yes! The new record is {current_time_in_sec:.2f} seconds.")
else:
    diff_time = abs(current_time_in_sec - record_in_seconds)
    print(f"No! He was {diff_time:.2f} seconds slower.")
