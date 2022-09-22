symbols = ["A", "a", "B", "b", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k",
           "L", "l", "M", "m", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w",
           "X", "x", "Y", "y", "Z", "z"]
count_c = 0
count_o = 0
count_n = 0
text = ""
while True:
    symbol = input()
    if symbol != "End":
        if symbol == "c":
            count_c += 1
            if count_c == 1:
                if count_c > 0 and count_o > 0 and count_n > 0:
                    text += " "
                    count_c = 0
                    count_o = 0
                    count_n = 0
                else:
                    continue
            else:
                text += symbol
        elif symbol == "o":
            count_o += 1
            if count_o == 1:
                if count_c > 0 and count_o > 0 and count_n > 0:
                    text += " "
                    count_c = 0
                    count_o = 0
                    count_n = 0
                else:
                    continue
            else:
                text += symbol
        elif symbol == "n":
            count_n += 1
            if count_n == 1:
                if count_c > 0 and count_o > 0 and count_n > 0:
                    text += " "
                    count_c = 0
                    count_o = 0
                    count_n = 0
                else:
                    continue
            else:
                text += symbol
        else:
            if symbol in symbols:
                text += symbol
            else:
                continue
    else:   # symbol == "End":
        print(text)
        break
