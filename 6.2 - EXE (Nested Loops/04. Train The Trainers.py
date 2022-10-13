sum_average_grades_per_all_presentation = 0
sum_grade_per_one_presentation = 0
count_presentations = 0
count_people_raters = int(input())
while True:
    name_presentation = input()
    if name_presentation == "Finish":
        average_grade_per_all_presentations = sum_average_grades_per_all_presentation / count_presentations
        print(f"Student's final assessment is {average_grade_per_all_presentations:.2f}.")
        break
    else:
        count_presentations += 1
        for rater in range(1, count_people_raters + 1):
            grade = float(input())
            sum_grade_per_one_presentation += grade
        average_grade_per_presentation = sum_grade_per_one_presentation / count_people_raters
        print(f"{name_presentation} - {average_grade_per_presentation:.2f}.")
        sum_average_grades_per_all_presentation += average_grade_per_presentation
        sum_grade_per_one_presentation = 0
