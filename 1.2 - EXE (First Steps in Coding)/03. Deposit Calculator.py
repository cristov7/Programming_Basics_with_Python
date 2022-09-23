deposit = float(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input()) / 100
final_sum = deposit + term_of_the_deposit * ((deposit * annual_interest_rate)/12)
print(final_sum)
