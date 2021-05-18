strings = input()

while not strings == "end":
    print(f"{strings} = {strings[::-1]}")
    strings = input()
