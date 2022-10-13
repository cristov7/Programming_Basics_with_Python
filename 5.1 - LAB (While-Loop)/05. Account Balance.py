total = 0
while True:
    contribution = input()
    if contribution == "NoMoreMoney":
        break
    else:
        contribution = float(contribution)
        if contribution < 0:
            print("Invalid operation!")
            break
        else:
            print(f"Increase: {contribution:.2f}")
            total += contribution
print(f"Total: {total:.2f}")
