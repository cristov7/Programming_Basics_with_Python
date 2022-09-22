max_count_fail_grade = int(input())
count_fail_grade = 0
number_of_problems = 0
last_problem_name = ""
sum_grades = 0
while True:
    name_of_the_exam = input()
    if name_of_the_exam != "Enough":
        grade_of_the_exam = int(input())
        number_of_problems += 1
        last_problem_name = name_of_the_exam
        sum_grades += grade_of_the_exam
        if grade_of_the_exam <= 4:
            count_fail_grade += 1
            if count_fail_grade == max_count_fail_grade:
                print(f"You need a break, {max_count_fail_grade} poor grades.")
                break
            else:
                continue
        else:
            continue
    else:   # name_of_the_exam == "Enough":
        average_score = sum_grades / number_of_problems
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {number_of_problems}")
        print(f"Last problem: {last_problem_name}")
        break
