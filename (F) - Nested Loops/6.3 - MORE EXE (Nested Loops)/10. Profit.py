money_1lv = int(input())
money_2lv = int(input())
money_5lv = int(input())
needed_sum = int(input())
leva_01 = 0
leva_02 = 0
leva_05 = 0
for leva_01 in range(money_1lv + 1):
    for leva_02 in range(money_2lv + 1):
        for leva_05 in range(money_5lv + 1):
            if ((leva_01 * 1) + (leva_02 * 2) + (leva_05 * 5)) == needed_sum:
                print(f"{leva_01} * 1 lv. + {leva_02} * 2 lv. + {leva_05} * 5 lv. = {needed_sum} lv.")
            else:
                continue
