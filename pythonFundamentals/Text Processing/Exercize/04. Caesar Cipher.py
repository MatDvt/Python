text = input()
new_text = ""
for symbol in text:
    new_letter = ord(symbol)
    new_letter += 3
    new_text += chr(new_letter)
print(new_text)
