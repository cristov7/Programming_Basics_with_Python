from math import ceil
height_wall = int(input())
width_wall = int(input())
percent_walls_not_for_paint = int(input()) / 100
walls_in_hall = 4
quadratic_m_per_hall = height_wall * width_wall * walls_in_hall
quadratic_m_to_paint = ceil(quadratic_m_per_hall - (quadratic_m_per_hall * percent_walls_not_for_paint))
while True:
    command = input()
    if command == "Tired!":
        print(f"{quadratic_m_to_paint} quadratic m left.")
        break
    else:
        liters_paint = int(command)
        if quadratic_m_to_paint > liters_paint:
            quadratic_m_to_paint -= liters_paint
        else:
            diff_paint = abs(quadratic_m_to_paint - liters_paint)
            if diff_paint == 0:
                print(f"All walls are painted! Great job, Pesho!")
                break
            else:
                print(f"All walls are painted and you have {diff_paint} l paint left!")
                break
