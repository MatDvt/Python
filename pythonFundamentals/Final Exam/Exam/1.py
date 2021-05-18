email = input()

data = input()
user_name = ""
asci_char = []

while not data.startswith("Complete"):
    if data.startswith("Make Upper"):
        email = email.upper()
        print(email)
    elif data.startswith("Make Lower"):
        email = email.lower()
        print(email)
    elif data.startswith("GetDomain"):
        current_command = data.split()
        position = int(current_command[1])
        last_n_chars = email[-position:]
        print(last_n_chars)

    elif data.startswith("GetUsername"):
        if not "@" in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            username = email.split("@")[0]
            print(username)
    elif data.startswith("Replace"):
        current_command = data.split()
        char_to_replace = current_command[1]
        print(email.replace(char_to_replace, "-"))
    elif data.startswith("Encrypt"):
        for c in email:
            asci_char.append(ord(c))
        print(*asci_char)
    data = input()
