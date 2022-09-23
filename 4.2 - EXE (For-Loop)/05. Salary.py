count_open_tabs = int(input())
salary = int(input())
final_salary = salary
for browsers in range(count_open_tabs):
    if final_salary > 0:
        name_per_website = input()
        if name_per_website == "Facebook":
            forfeit = 150
            final_salary -= forfeit
        elif name_per_website == "Instagram":
            forfeit = 100
            final_salary -= forfeit
        elif name_per_website == "Reddit":
            forfeit = 50
            final_salary -= forfeit
        else:
            continue
if final_salary > 0:
    print(final_salary)
else:
    print("You have lost your salary.")
