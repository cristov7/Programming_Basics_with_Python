type_of_fruit = input()
day_of_the_week = input()
quantity = float(input())
the_bill_is = 0
if day_of_the_week == "Monday"\
        or day_of_the_week == "Tuesday"\
        or day_of_the_week == "Wednesday"\
        or day_of_the_week == "Thursday"\
        or day_of_the_week == "Friday":
    if type_of_fruit == "banana":
        price_per_product = 2.50
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    elif type_of_fruit == "apple":
        price_per_product = 1.20
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    elif type_of_fruit == "orange":
        price_per_product = 0.85
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    elif type_of_fruit == "grapefruit":
        price_per_product = 1.45
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    elif type_of_fruit == "kiwi":
        price_per_product = 2.70
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    elif type_of_fruit == "pineapple":
        price_per_product = 5.50
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    elif type_of_fruit == "grapes":
        price_per_product = 3.85
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    else:
        print("error")
elif day_of_the_week == "Saturday"\
        or day_of_the_week == "Sunday":
    if type_of_fruit == "banana":
        price_per_product = 2.70
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    elif type_of_fruit == "apple":
        price_per_product = 1.25
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    elif type_of_fruit == "orange":
        price_per_product = 0.90
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    elif type_of_fruit == "grapefruit":
        price_per_product = 1.60
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    elif type_of_fruit == "kiwi":
        price_per_product = 3.00
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    elif type_of_fruit == "pineapple":
        price_per_product = 5.60
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    elif type_of_fruit == "grapes":
        price_per_product = 4.20
        the_bill_is = quantity * price_per_product
        print(f"{the_bill_is:.2f}")
    else:
        print("error")
else:
    print("error")
