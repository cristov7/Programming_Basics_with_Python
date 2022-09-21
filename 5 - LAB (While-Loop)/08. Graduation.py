name = input()
fail = 0
school_class = 1
sum_grades = 0
while school_class < 13:
    grade = float(input())
    if grade < 4.00:
        fail += 1
        if fail > 1:
            print(f"{name} has been excluded at {school_class} grade")
            break
        else:
            continue
    else:
        sum_grades += grade
        school_class += 1
        if school_class == 13:
            average_grade = sum_grades / 12
            print(f"{name} graduated. Average grade: {average_grade:.2f}")
            break
        else:
            continue
