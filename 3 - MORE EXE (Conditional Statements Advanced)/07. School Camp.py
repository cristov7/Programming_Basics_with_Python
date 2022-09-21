season = input()
type_group = input()
count_students = int(input())
count_nights = int(input())
sport = ""
price_per_one_night = 0
discount = 0
if season == "Winter":
    if type_group == "boys":
        sport = "Judo"
        price_per_one_night = 9.60
        if 10 <= count_students < 20:
            discount = price_per_one_night * 0.05
            price_per_one_night -= discount
        elif 20 <= count_students < 50:
            discount = price_per_one_night * 0.15
            price_per_one_night -= discount
        elif count_students >= 50:
            discount = price_per_one_night * 0.50
            price_per_one_night -= discount
    elif type_group == "girls":
        sport = "Gymnastics"
        price_per_one_night = 9.60
        if 10 <= count_students < 20:
            discount = price_per_one_night * 0.05
            price_per_one_night -= discount
        elif 20 <= count_students < 50:
            discount = price_per_one_night * 0.15
            price_per_one_night -= discount
        elif count_students >= 50:
            discount = price_per_one_night * 0.50
            price_per_one_night -= discount
    elif type_group == "mixed":
        sport = "Ski"
        price_per_one_night = 10
        if 10 <= count_students < 20:
            discount = price_per_one_night * 0.05
            price_per_one_night -= discount
        elif 20 <= count_students < 50:
            discount = price_per_one_night * 0.15
            price_per_one_night -= discount
        elif count_students >= 50:
            discount = price_per_one_night * 0.50
            price_per_one_night -= discount
elif season == "Spring":
    if type_group == "boys":
        sport = "Tennis"
        price_per_one_night = 7.20
        if 10 <= count_students < 20:
            discount = price_per_one_night * 0.05
            price_per_one_night -= discount
        elif 20 <= count_students < 50:
            discount = price_per_one_night * 0.15
            price_per_one_night -= discount
        elif count_students >= 50:
            discount = price_per_one_night * 0.50
            price_per_one_night -= discount
    elif type_group == "girls":
        sport = "Athletics"
        price_per_one_night = 7.20
        if 10 <= count_students < 20:
            discount = price_per_one_night * 0.05
            price_per_one_night -= discount
        elif 20 <= count_students < 50:
            discount = price_per_one_night * 0.15
            price_per_one_night -= discount
        elif count_students >= 50:
            discount = price_per_one_night * 0.50
            price_per_one_night -= discount
    elif type_group == "mixed":
        sport = "Cycling"
        price_per_one_night = 9.50
        if 10 <= count_students < 20:
            discount = price_per_one_night * 0.05
            price_per_one_night -= discount
        elif 20 <= count_students < 50:
            discount = price_per_one_night * 0.15
            price_per_one_night -= discount
        elif count_students >= 50:
            discount = price_per_one_night * 0.50
            price_per_one_night -= discount
elif season == "Summer":
    if type_group == "boys":
        sport = "Football"
        price_per_one_night = 15
        if 10 <= count_students < 20:
            discount = price_per_one_night * 0.05
            price_per_one_night -= discount
        elif 20 <= count_students < 50:
            discount = price_per_one_night * 0.15
            price_per_one_night -= discount
        elif count_students >= 50:
            discount = price_per_one_night * 0.50
            price_per_one_night -= discount
    elif type_group == "girls":
        sport = "Volleyball"
        price_per_one_night = 15
        if 10 <= count_students < 20:
            discount = price_per_one_night * 0.05
            price_per_one_night -= discount
        elif 20 <= count_students < 50:
            discount = price_per_one_night * 0.15
            price_per_one_night -= discount
        elif count_students >= 50:
            discount = price_per_one_night * 0.50
            price_per_one_night -= discount
    elif type_group == "mixed":
        sport = "Swimming"
        price_per_one_night = 20
        if 10 <= count_students < 20:
            discount = price_per_one_night * 0.05
            price_per_one_night -= discount
        elif 20 <= count_students < 50:
            discount = price_per_one_night * 0.15
            price_per_one_night -= discount
        elif count_students >= 50:
            discount = price_per_one_night * 0.50
            price_per_one_night -= discount
final_price_per_one_student = price_per_one_night * count_nights
final_price_per_all_students = final_price_per_one_student * count_students
print(f"{sport} {final_price_per_all_students:.2f} lv.")
