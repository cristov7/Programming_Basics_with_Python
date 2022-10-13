count_students = int(input())
students_between_2_and_3 = 0
students_between_3_and_4 = 0
students_between_4_and_5 = 0
students_between_5_and_6 = 0
sum_grades = 0
for grades in range(count_students):
    grade = float(input())
    sum_grades += grade
    if 2 <= grade <= 2.99:
        students_between_2_and_3 += 1
    elif 3 <= grade <= 3.99:
        students_between_3_and_4 += 1
    elif 4 <= grade <= 4.99:
        students_between_4_and_5 += 1
    elif 5 <= grade <= 6:
        students_between_5_and_6 += 1
percent_students_between_2_and_3 = (students_between_2_and_3 / count_students) * 100
percent_students_between_3_and_4 = (students_between_3_and_4 / count_students) * 100
percent_students_between_4_and_5 = (students_between_4_and_5 / count_students) * 100
percent_students_between_5_and_6 = (students_between_5_and_6 / count_students) * 100
average_grade = sum_grades / count_students
print(f"Top students: {percent_students_between_5_and_6:.2f}%")
print(f"Between 4.00 and 4.99: {percent_students_between_4_and_5:.2f}%")
print(f"Between 3.00 and 3.99: {percent_students_between_3_and_4:.2f}%")
print(f"Fail: {percent_students_between_2_and_3:.2f}%")
print(f"Average: {average_grade:.2f}")
