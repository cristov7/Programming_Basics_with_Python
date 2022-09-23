count_students_between_2_and_3 = 0
count_students_between_3_and_4 = 0
count_students_between_4_and_5 = 0
count_students_between_5_and_6 = 0
sum_degrees = 0
count_students = int(input())
for students in range(count_students):
    degree = float(input())
    sum_degrees += degree
    if 2 <= degree <= 2.99:
        count_students_between_2_and_3 += 1
    elif 3 <= degree <= 3.99:
        count_students_between_3_and_4 += 1
    elif 4 <= degree <= 4.99:
        count_students_between_4_and_5 += 1
    elif 5 <= degree <= 6:
        count_students_between_5_and_6 += 1
percent_students_between_2_and_3 = (count_students_between_2_and_3 / count_students) * 100
percent_students_between_3_and_4 = (count_students_between_3_and_4 / count_students) * 100
percent_students_between_4_and_5 = (count_students_between_4_and_5 / count_students) * 100
percent_students_between_5_and_6 = (count_students_between_5_and_6 / count_students) * 100
average_grade = sum_degrees / count_students
print(f"Top students: {percent_students_between_5_and_6:.2f}%")
print(f"Between 4.00 and 4.99: {percent_students_between_4_and_5:.2f}%")
print(f"Between 3.00 and 3.99: {percent_students_between_3_and_4:.2f}%")
print(f"Fail: {percent_students_between_2_and_3:.2f}%")
print(f"Average: {average_grade:.2f}")
