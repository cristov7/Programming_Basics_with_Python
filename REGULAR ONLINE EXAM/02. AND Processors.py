target_count_processors = int(input())
count_employees = int(input())
working_days = int(input())
one_working_day_in_hours = 8
one_processor_in_hours = 3
price_per_one_processor = 110.10
target_price_per_processors = target_count_processors * price_per_one_processor
total_work_in_hours = count_employees * working_days * one_working_day_in_hours
total_ready_processors = total_work_in_hours // one_processor_in_hours
total_price_per_processors = total_ready_processors * price_per_one_processor
if total_price_per_processors > target_price_per_processors:
    profit = abs(total_price_per_processors - target_price_per_processors)
    print(f"Profit: -> {profit:.2f} BGN")
else:
    losses = abs(total_price_per_processors - target_price_per_processors)
    print(f"Losses: -> {losses:.2f} BGN")
