def check_password_is_valid(pword):
    is_valid = True
    consist_only_of_letter_and_digits = True
    count_digit = 0

    if len(pword) < 6 or len(pword) > 10:
        print(f"Password must be between 6 and 10 characters")
        is_valid = False
    for el in pword:
        if el.isdigit():
            count_digit += 1

        if not el.isdigit() and not el.isalpha():
            is_valid = False
            consist_only_of_letter_and_digits = False

    if not consist_only_of_letter_and_digits:
        print(f'Password must consist only of letters and digits')

    if count_digit < 2:
        is_valid = False
        print(f'Password must have at least 2 digits')

    return is_valid


password = input()
result = check_password_is_valid(password)

if result:
    print(f'Password is valid')

