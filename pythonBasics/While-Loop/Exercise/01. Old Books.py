searched_book = input()

books_count = 0
current_book = input()
while current_book != searched_book:
    if current_book == 'No More Books':
        break
    books_count += 1
    current_book = input()
if current_book == 'No More Books':
    print('The book you search is not here!')
    print(f'You checked {books_count} books.')
else:
    print(f'You checked {books_count} books and found it.')
