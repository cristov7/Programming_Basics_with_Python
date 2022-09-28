number = int(input())
counter = 0
while True:
    counter += 1
    for column in range(1, counter + 1):
        dollar = "$"
        print(dollar, end=" ")
    print()
    if counter == number:
        break
    else:
        continue
