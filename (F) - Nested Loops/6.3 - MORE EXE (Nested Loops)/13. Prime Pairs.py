first_start = int(input())
second_start = int(input())
first_diff = int(input())
second_diff = int(input())
first_stop = first_start + first_diff
second_stop = second_start + second_diff
first_prime_bool = False
second_prime_bool = False
for first_number in range(first_start, first_stop + 1):
    first_counter = 0
    for first_prime in range(1, first_number + 1):
        if first_number % first_prime == 0:
            first_counter += 1
        else:
            continue
    if first_counter == 2:
        first_prime_bool = True
    if first_prime_bool:
        for second_number in range(second_start, second_stop + 1):
            second_counter = 0
            for second_prime in range(1, second_number + 1):
                if second_number % second_prime == 0:
                    second_counter += 1
                else:
                    continue
            if second_counter == 2:
                second_prime_bool = True
            if first_prime_bool and second_prime_bool:
                print(f"{first_number}{second_number}")
                second_prime_bool = False
            else:
                continue
        first_prime_bool = False
    else:
        continue
