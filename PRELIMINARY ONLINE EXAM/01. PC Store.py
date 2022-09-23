# 1 долар = 1.57 лв.
price_per_processors_in_dollars = float(input())
price_per_video_cards_in_dollars = float(input())
price_per_one_ram_memory_in_dollars = float(input())
count_ram_memories = int(input())
percent_discount = float(input())
full_price_per_processors_in_dollars = price_per_processors_in_dollars - (price_per_processors_in_dollars * percent_discount)
full_price_per_video_card_in_dollars = price_per_video_cards_in_dollars - (price_per_video_cards_in_dollars * percent_discount)
full_price_per_ram_memories_in_dollars = price_per_one_ram_memory_in_dollars * count_ram_memories
full_price_in_dollars = full_price_per_processors_in_dollars + full_price_per_video_card_in_dollars + full_price_per_ram_memories_in_dollars
final_price_in_lv = full_price_in_dollars * 1.57
print(f"Money needed - {final_price_in_lv:.2f} leva.")
