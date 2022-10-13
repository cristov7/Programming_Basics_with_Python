number = int(input())
counter = 0
while True:
    counter += 1
    for row in range(1, counter + 1):
        dollar = "$"
        print(f"{dollar}", end=" ")
    print()
    if counter == number:
        break
    else:
        continue
