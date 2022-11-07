max_fans_per_stadium = int(input())
count_all_fans = int(input())
count_fans_in_sector_A = 0
count_fans_in_sector_B = 0
count_fans_in_sector_V = 0
count_fans_in_sector_G = 0
# count_fans_for_home_team = 0
# count_fans_for_guest_team = 0
for fan in range(count_all_fans):
    sector = input()
    # if sector == "A" or sector == "B":
    #     count_fans_for_home_team += 1
    # elif sector == "V" or sector == "G":
    #     count_fans_for_guest_team += 1
    if sector == "A":
        count_fans_in_sector_A += 1
    elif sector == "B":
        count_fans_in_sector_B += 1
    elif sector == "V":
        count_fans_in_sector_V += 1
    elif sector == "G":
        count_fans_in_sector_G += 1
percent_count_fans_in_sector_A = (count_fans_in_sector_A / count_all_fans) * 100
percent_count_fans_in_sector_B = (count_fans_in_sector_B / count_all_fans) * 100
percent_count_fans_in_sector_V = (count_fans_in_sector_V / count_all_fans) * 100
percent_count_fans_in_sector_G = (count_fans_in_sector_G / count_all_fans) * 100
percent_count_all_fans = (count_all_fans / max_fans_per_stadium) * 100
# percent_count_fans_for_home_team = (count_fans_for_home_team / max_fans_per_stadium) * 100
# percent_count_fans_for_guest_team = (count_fans_for_guest_team / max_fans_per_stadium) * 100
print(f"{percent_count_fans_in_sector_A:.2f}%")
print(f"{percent_count_fans_in_sector_B:.2f}%")
print(f"{percent_count_fans_in_sector_V:.2f}%")
print(f"{percent_count_fans_in_sector_G:.2f}%")
# print(f"{percent_count_fans_for_home_team:.2f}%")
# print(f"{percent_count_fans_for_guest_team:.2f}%")
print(f"{percent_count_all_fans:.2f}%")
