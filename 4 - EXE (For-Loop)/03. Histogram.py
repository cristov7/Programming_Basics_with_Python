count_numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for numbers in range(count_numbers):
    number = int(input())
    if 1 <= number < 200:
        p1 += 1
    elif 200 <= number < 400:
        p2 += 1
    elif 400 <= number < 600:
        p3 += 1
    elif 600 <= number < 800:
        p4 += 1
    elif 800 <= number <= 1000:
        p5 += 1
p1_in_percent = (p1 / count_numbers) * 100
p2_in_percent = (p2 / count_numbers) * 100
p3_in_percent = (p3 / count_numbers) * 100
p4_in_percent = (p4 / count_numbers) * 100
p5_in_percent = (p5 / count_numbers) * 100
print(f"{p1_in_percent:.2f}%")
print(f"{p2_in_percent:.2f}%")
print(f"{p3_in_percent:.2f}%")
print(f"{p4_in_percent:.2f}%")
print(f"{p5_in_percent:.2f}%")
