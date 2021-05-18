import re

n = int(input())

for i in range(n):
    text = input()
    pattern = r"([!])(?P<command>[A-Z][a-z]{2,})(\1):(\[)(?P<message>[a-zA-Z]{7,})(\])"
    match = re.search(pattern, text)

    if match is None:
        print("The message is invalid")
        continue

    command = match.group("command")
    message = match.group("message")

    encrypted_message = ""

    for char in message:
        encrypted_message += str(ord(char)) + " "

    print(f'{command}: {encrypted_message}')
