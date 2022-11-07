V_pool_in_liters = int(input())
P1_debit_per_one_hour = int(input())
P2_debit_per_one_hour = int(input())
H_hours_without_worker = float(input())
total_P1_debit_in_liters = P1_debit_per_one_hour * H_hours_without_worker
total_P2_debit_in_liters = P2_debit_per_one_hour * H_hours_without_worker
total_P1_debit_and_P2_debit_in_liters = total_P1_debit_in_liters + total_P2_debit_in_liters
if V_pool_in_liters >= total_P1_debit_and_P2_debit_in_liters:
    total_P1_debit_and_P2_debit_in_percent = (total_P1_debit_and_P2_debit_in_liters / V_pool_in_liters) * 100
    total_P1_debit_in_percent = (total_P1_debit_in_liters / total_P1_debit_and_P2_debit_in_liters) * 100
    total_P2_debit_in_percent = (total_P2_debit_in_liters / total_P1_debit_and_P2_debit_in_liters) * 100
    print(f"The pool is {total_P1_debit_and_P2_debit_in_percent:.2f}% full. Pipe 1: {total_P1_debit_in_percent:.2f}%. Pipe 2: {total_P2_debit_in_percent:.2f}%.")
else:
    excess_water_in_liters = abs(V_pool_in_liters - total_P1_debit_and_P2_debit_in_liters)
    print(f"For {H_hours_without_worker:.2f} hours the pool overflows with {excess_water_in_liters:.2f} liters.")
