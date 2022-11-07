count_tickets_per_one_movie = 0
count_all_student_tickets = 0
count_all_standard_tickets = 0
count_all_kid_tickets = 0
count_all_tickets = 0
while True:
    name_movie = input()
    if name_movie == "Finish":
        print(f"Total tickets: {count_all_tickets}")
        percent_all_student_tickets = (count_all_student_tickets / count_all_tickets) * 100
        print(f"{percent_all_student_tickets:.2f}% student tickets.")
        percent_all_standard_tickets = (count_all_standard_tickets / count_all_tickets) * 100
        print(f"{percent_all_standard_tickets:.2f}% standard tickets.")
        percent_all_kid_tickets = (count_all_kid_tickets / count_all_tickets) * 100
        print(f"{percent_all_kid_tickets:.2f}% kids tickets.")
        break
    else:
        free_places_per_projection = int(input())
        for free_place in range(free_places_per_projection):
            type_ticket = input()   # "student" / "standard" / "kid"
            if type_ticket == "End":
                break
            else:
                if type_ticket == "student":
                    count_tickets_per_one_movie += 1
                    count_all_student_tickets += 1
                    count_all_tickets += 1
                elif type_ticket == "standard":
                    count_tickets_per_one_movie += 1
                    count_all_standard_tickets += 1
                    count_all_tickets += 1
                elif type_ticket == "kid":
                    count_tickets_per_one_movie += 1
                    count_all_kid_tickets += 1
                    count_all_tickets += 1
        if free_places_per_projection != 0:
            percent_not_free_places = (count_tickets_per_one_movie / free_places_per_projection) * 100
            print(f"{name_movie} - {percent_not_free_places:.2f}% full.")
            count_tickets_per_one_movie = 0
        else:
            continue
