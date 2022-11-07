text = input()
vowels_value_sum = 0
for symbols in range(len(text)):
    if text[symbols] == "a":
        vowels_value_sum += 1
    elif text[symbols] == "e":
        vowels_value_sum += 2
    elif text[symbols] == "i":
        vowels_value_sum += 3
    elif text[symbols] == "o":
        vowels_value_sum += 4
    elif text[symbols] == "u":
        vowels_value_sum += 5
    else:
        continue
print(vowels_value_sum)
