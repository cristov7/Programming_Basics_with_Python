count_pages = int(input())
number_of_reads_pages_per_one_hour = int(input())
count_days_to_read_all = int(input())
full_hours_to_read = count_pages // number_of_reads_pages_per_one_hour
hours_to_read_per_day = full_hours_to_read / count_days_to_read_all
print(int(hours_to_read_per_day))
