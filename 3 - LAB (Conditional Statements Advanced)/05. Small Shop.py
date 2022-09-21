product = input()
city = input()
quantity = float(input())
the_bill_is = 0
if city == "Sofia":
    if product == "coffee":
        price_per_product = 0.50
        the_bill_is = quantity * price_per_product
    elif product == "water":
        price_per_product = 0.80
        the_bill_is = quantity * price_per_product
    elif product == "beer":
        price_per_product = 1.20
        the_bill_is = quantity * price_per_product
    elif product == "sweets":
        price_per_product = 1.45
        the_bill_is = quantity * price_per_product
    elif product == "peanuts":
        price_per_product = 1.60
        the_bill_is = quantity * price_per_product
elif city == "Plovdiv":
    if product == "coffee":
        price_per_product = 0.40
        the_bill_is = quantity * price_per_product
    elif product == "water":
        price_per_product = 0.70
        the_bill_is = quantity * price_per_product
    elif product == "beer":
        price_per_product = 1.15
        the_bill_is = quantity * price_per_product
    elif product == "sweets":
        price_per_product = 1.30
        the_bill_is = quantity * price_per_product
    elif product == "peanuts":
        price_per_product = 1.50
        the_bill_is = quantity * price_per_product
elif city == "Varna":
    if product == "coffee":
        price_per_product = 0.45
        the_bill_is = quantity * price_per_product
    elif product == "water":
        price_per_product = 0.70
        the_bill_is = quantity * price_per_product
    elif product == "beer":
        price_per_product = 1.10
        the_bill_is = quantity * price_per_product
    elif product == "sweets":
        price_per_product = 1.35
        the_bill_is = quantity * price_per_product
    elif product == "peanuts":
        price_per_product = 1.55
        the_bill_is = quantity * price_per_product
print(the_bill_is)
