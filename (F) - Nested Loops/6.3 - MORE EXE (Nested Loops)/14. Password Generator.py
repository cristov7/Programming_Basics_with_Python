first_number = int(input())
second_number = int(input())
ord_letter = 97 + second_number
for number_1 in range(1, first_number):
    for number_2 in range(1, first_number):
        for ord_1 in range(97, ord_letter):
            for ord_2 in range(97, ord_letter):
                for number_3 in range(1, first_number + 1):
                    if number_1 < number_3 and number_2 < number_3:
                        char_1 = chr(ord_1)
                        char_2 = chr(ord_2)
                        print(f"{number_1}{number_2}{char_1}{char_2}{number_3}", end=" ")
                    else:
                        continue
