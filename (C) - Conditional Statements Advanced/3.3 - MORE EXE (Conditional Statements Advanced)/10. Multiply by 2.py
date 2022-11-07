while True:
    number = float(input())
    if number >= 0:
        result = number * 2
        print(f"Result: {result:.2f}")
    else:
        print("Negative number!")
        break
