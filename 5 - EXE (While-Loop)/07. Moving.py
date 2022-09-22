width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
total_free_space = width_free_space * length_free_space * height_free_space
width_per_box = 1
length_per_box = 1
height_per_box = 1
total_per_box = width_per_box * length_per_box * height_per_box
max_count_boxes = total_free_space // total_per_box
count_boxes = 0
while True:
    command = input()
    if command == "Done":
        left_free_space = max_count_boxes
        print(f"{left_free_space} Cubic meters left.")
        break
    else:
        count_boxes = int(command) * total_per_box
        if count_boxes <= max_count_boxes:
            max_count_boxes -= count_boxes
        else:
            needed_more_free_space = abs(count_boxes - max_count_boxes)
            print(f"No more free space! You need {needed_more_free_space} Cubic meters more.")
            break
