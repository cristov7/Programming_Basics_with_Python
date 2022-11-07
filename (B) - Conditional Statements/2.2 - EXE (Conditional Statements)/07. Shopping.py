the_peters_budget = float(input())
count_video_cards = int(input())
count_processors = int(input())
count_ram_memories = int(input())
price_per_one_video_card = 250
full_price_per_video_cards = count_video_cards * price_per_one_video_card
price_per_one_processor = full_price_per_video_cards * 0.35
price_per_one_ram_memory = full_price_per_video_cards * 0.10
full_price_per_processors = count_processors * price_per_one_processor
full_price_per_ram_memories = count_ram_memories * price_per_one_ram_memory
full_price_per_all = full_price_per_video_cards + full_price_per_processors + full_price_per_ram_memories
discount = 0
if count_video_cards > count_processors:
    discount = full_price_per_all * 0.15
final_price_per_all = full_price_per_all - discount
if the_peters_budget >= final_price_per_all:
    money_left_over = abs(the_peters_budget - final_price_per_all)
    print(f"You have {money_left_over:.2f} leva left!")
else:
    not_enough_money = abs(the_peters_budget - final_price_per_all)
    print(f"Not enough money! You need {not_enough_money:.2f} leva more!")
