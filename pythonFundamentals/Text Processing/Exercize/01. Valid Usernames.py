def valid_username(username):
    if len(username) < 3 or len(username) > 16:
        return False
    for el in username:
        if not el.isdigit() and not el.isalpha() and not el == "-" and not el == "_":
            return False
    return True


data = input().split(", ")
valid_user = []

for element in data:
    if valid_username(element):
        valid_user.append(element)
print(f"\n".join(valid_user))
