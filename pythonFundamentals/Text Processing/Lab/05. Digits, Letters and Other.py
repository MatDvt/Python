letters = ""
nums = ""
others = ""

text = input()

for char in text:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        nums += char
    else:
        others += char
print(nums)
print(letters)
print(others)
