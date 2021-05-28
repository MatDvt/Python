def read_contacts():
    contacts = {}
    while True:
        text = input()
        if text.isnumeric():
            break
        name, phone = text.split("-")
        contacts[name] = phone

    return contacts, int(text)


def print_person_n_times(n):
    for _ in range(n):
        name = input()

        if name in contacts:
            print(f"{name} -> {contacts[name]}")
        else:
            print(f"Contact {name} does not exist.")


contacts, n = read_contacts()
print_person_n_times(n)
