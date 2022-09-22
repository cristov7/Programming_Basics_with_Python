expected_sum = int(input())
sell_products_sum = 0
counter = 0
counter_per_cash = 0
counter_per_card = 0
sum_cash_payment = 0
sum_payment_by_card = 0
while True:
    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    else:
        price_per_products = int(command)
        counter += 1
        if counter % 2 != 0:   # odd
            cash_payment = price_per_products
            if cash_payment > 100:
                print("Error in transaction!")
            else:
                print("Product sold!")
                counter_per_cash += 1
                sell_products_sum += cash_payment
                sum_cash_payment += cash_payment
                if sell_products_sum >= expected_sum:
                    average_cash_payment = sum_cash_payment / counter_per_cash
                    average_payment_by_card = sum_payment_by_card / counter_per_card
                    print(f"Average CS: {average_payment_by_card:.2f}")
                    print(f"Average CC: {average_payment_by_card:.2f}")
                    break
                else:
                    continue
        else:   # even
            payment_by_card = price_per_products
            if payment_by_card < 10:
                print("Error in transaction!")
            else:
                print("Product sold!")
                counter_per_card += 1
                sell_products_sum += payment_by_card
                sum_payment_by_card += payment_by_card
                if sell_products_sum >= expected_sum:
                    average_cash_payment = sum_cash_payment / counter_per_cash
                    average_payment_by_card = sum_payment_by_card / counter_per_card
                    print(f"Average CS: {average_cash_payment:.2f}")
                    print(f"Average CC: {average_payment_by_card:.2f}")
                    break
                else:
                    continue
