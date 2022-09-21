count_groups_climber = int(input())
people_to_Musala = 0
people_to_Mont_Blanc = 0
people_to_Kilimanjaro = 0
people_to_K2 = 0
people_to_Everest = 0
for groups in range(count_groups_climber):
    people_in_group = int(input())
    if 1 <= people_in_group <= 5:
        people_to_Musala += people_in_group
    elif 6 <= people_in_group <= 12:
        people_to_Mont_Blanc += people_in_group
    elif 13 <= people_in_group <= 25:
        people_to_Kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        people_to_K2 += people_in_group
    elif people_in_group >= 41:
        people_to_Everest += people_in_group
all_people = people_to_Musala + people_to_Mont_Blanc + people_to_Kilimanjaro + people_to_K2 + people_to_Everest
percent_people_to_Musala = 0
if people_to_Musala != 0:
    percent_people_to_Musala = people_to_Musala / all_people * 100
else:
    percent_people_to_Musala = 0
percent_people_to_Mont_Blanc = 0
if people_to_Mont_Blanc != 0:
    percent_people_to_Mont_Blanc = people_to_Mont_Blanc / all_people * 100
else:
    percent_people_to_Mont_Blanc = 0
percent_people_to_Kilimanjaro = 0
if people_to_Kilimanjaro != 0:
    percent_people_to_Kilimanjaro = people_to_Kilimanjaro / all_people * 100
else:
    percent_people_to_Kilimanjaro = 0
percent_people_to_K2 = 0
if people_to_K2 != 0:
    percent_people_to_K2 = people_to_K2 / all_people * 100
else:
    percent_people_to_K2 = 0
percent_people_to_Everest = 0
if people_to_Everest != 0:
    percent_people_to_Everest = people_to_Everest / all_people * 100
else:
    percent_people_to_Everest = 0
print(f"{percent_people_to_Musala:.2f}%")
print(f"{percent_people_to_Mont_Blanc:.2f}%")
print(f"{percent_people_to_Kilimanjaro:.2f}%")
print(f"{percent_people_to_K2:.2f}%")
print(f"{percent_people_to_Everest:.2f}%")
