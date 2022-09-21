import sys
min_number = sys.maxsize
while True:
    command = input()
    if command == "Stop":
        break
    else:
        command = int(command)
        if command < min_number:
            min_number = command
        else:
            continue
print(min_number)
