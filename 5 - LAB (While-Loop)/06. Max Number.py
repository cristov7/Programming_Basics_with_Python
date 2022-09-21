import sys
max_number = - sys.maxsize
while True:
    command = input()
    if command == "Stop":
        break
    else:
        command = int(command)
        if command > max_number:
            max_number = command
        else:
            continue
print(max_number)
