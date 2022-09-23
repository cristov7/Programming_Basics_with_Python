price_per_hall = int(input())
price_per_statuettes = price_per_hall * 0.70
price_per_catering = price_per_statuettes * 0.85
price_per_voicing = price_per_catering / 2
expenses = price_per_hall + price_per_statuettes + price_per_catering + price_per_voicing
print(f"{expenses:.2f}")
