count_transportations = int(input())
total_price = 0
total_tones = 0
transported_tones_with_buses = 0
transported_tones_with_trucks = 0
transported_tones_with_trains = 0
for transportation in range(count_transportations):
    freight_in_tones = int(input())
    total_tones += freight_in_tones
    if 0 < freight_in_tones <= 3:
        transported_tones_with_buses += freight_in_tones
        price_per_ton = 200
        total_price += price_per_ton * freight_in_tones
    elif 4 <= freight_in_tones <= 11:
        transported_tones_with_trucks += freight_in_tones
        price_per_ton = 175
        total_price += price_per_ton * freight_in_tones
    elif 12 <= freight_in_tones:
        transported_tones_with_trains += freight_in_tones
        price_per_ton = 120
        total_price += price_per_ton * freight_in_tones
average_total_price = total_price / total_tones
percent_transported_tones_with_buses = (transported_tones_with_buses / total_tones) * 100
percent_transported_tones_with_trucks = (transported_tones_with_trucks / total_tones) * 100
percent_transported_tones_with_trains = (transported_tones_with_trains / total_tones) * 100
print(f"{average_total_price:.2f}")
print(f"{percent_transported_tones_with_buses:.2f}%")
print(f"{percent_transported_tones_with_trucks:.2f}%")
print(f"{percent_transported_tones_with_trains:.2f}%")
