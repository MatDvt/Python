def check_if_palindrome(element):
    if element == element[::-1]:  # slicing - you can check the reverse value of a string
        return True
    return False


lst_of_str = input().split(", ")

for el in lst_of_str:
    is_palindrome = check_if_palindrome(el)
    if is_palindrome:
        print(True)
    else:
        print(False)
