sum_prime_numbers = 0
sum_non_prime_numbers = 0
command = input()
while command != "stop":
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
    else:
        current_number_is_prime = True
        for numbers in range(2, current_number):
            if current_number % numbers == 0:
                current_number_is_prime = False
                break
        if current_number_is_prime:
            sum_prime_numbers += current_number
        else:
            sum_non_prime_numbers += current_number
    command = input()
print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")


# sum_prime_value = 0
# sum_non_prime_value = 0
# while True:
#     command = input()
#     if command != "stop":
#         number = int(command)
#         if number >= 0:  # (positive + 0)
#             if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number == 1 and number != 0:  # (prime + non)
#                 if number == 2 or number == 3 or number == 5 or number == 7:  # prime
#                     sum_prime_value += number
#                 else:  # non prime
#                     sum_non_prime_value += number
#             else:  # prime
#                 sum_prime_value += number
#         else:  # negative
#             print("Number is negative.")
#             continue
#     else:
#         break
# print(f"Sum of all prime numbers is: {sum_prime_value}")
# print(f"Sum of all non prime numbers is: {sum_non_prime_value}")
