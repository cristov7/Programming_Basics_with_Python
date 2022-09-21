city = input()
sales_volume = float(input())
final_trade_commission = 0
if city == "Sofia":
    if 0 <= sales_volume <= 500:
        trade_commission_in_percent = 0.05
        final_trade_commission = sales_volume * trade_commission_in_percent
        print(f"{final_trade_commission:.2f}")
    elif 500 < sales_volume <= 1000:
        trade_commission_in_percent = 0.07
        final_trade_commission = sales_volume * trade_commission_in_percent
        print(f"{final_trade_commission:.2f}")
    elif 1000 < sales_volume <= 10000:
        trade_commission_in_percent = 0.08
        final_trade_commission = sales_volume * trade_commission_in_percent
        print(f"{final_trade_commission:.2f}")
    elif sales_volume > 10000:
        trade_commission_in_percent = 0.12
        final_trade_commission = sales_volume * trade_commission_in_percent
        print(f"{final_trade_commission:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= sales_volume <= 500:
        trade_commission_in_percent = 0.045
        final_trade_commission = sales_volume * trade_commission_in_percent
        print(f"{final_trade_commission:.2f}")
    elif 500 < sales_volume <= 1000:
        trade_commission_in_percent = 0.075
        final_trade_commission = sales_volume * trade_commission_in_percent
        print(f"{final_trade_commission:.2f}")
    elif 1000 < sales_volume <= 10000:
        trade_commission_in_percent = 0.10
        final_trade_commission = sales_volume * trade_commission_in_percent
        print(f"{final_trade_commission:.2f}")
    elif sales_volume > 10000:
        trade_commission_in_percent = 0.13
        final_trade_commission = sales_volume * trade_commission_in_percent
        print(f"{final_trade_commission:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        trade_commission_in_percent = 0.055
        final_trade_commission = sales_volume * trade_commission_in_percent
        print(f"{final_trade_commission:.2f}")
    elif 500 < sales_volume <= 1000:
        trade_commission_in_percent = 0.08
        final_trade_commission = sales_volume * trade_commission_in_percent
        print(f"{final_trade_commission:.2f}")
    elif 1000 < sales_volume <= 10000:
        trade_commission_in_percent = 0.12
        final_trade_commission = sales_volume * trade_commission_in_percent
        print(f"{final_trade_commission:.2f}")
    elif sales_volume > 10000:
        trade_commission_in_percent = 0.145
        final_trade_commission = sales_volume * trade_commission_in_percent
        print(f"{final_trade_commission:.2f}")
    else:
        print("error")
else:
    print("error")
