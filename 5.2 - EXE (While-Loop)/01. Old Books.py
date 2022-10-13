wanted_book = input()
count_searched_books = 0
while True:
    name_of_the_book = input()
    if name_of_the_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count_searched_books} books.")
        break
    elif name_of_the_book == wanted_book:
        print(f"You checked {count_searched_books} books and found it.")
        break
    else:
        count_searched_books += 1
        continue
