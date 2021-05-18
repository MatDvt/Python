def register(side, user, fbook):
    for sd, us in fbook.items():
        if user in us:
            return fbook
    if side not in fbook:
        fbook[side] = [user]
    else:
        if user not in fbook[side]:
            fbook[side].append(user)
    return fbook


command = input()
forceBook = {}

while command != 'Lumpawaroo':
    if '|' in command:
        s, u = command.split(' | ')
        forceBook = register(s, u, forceBook)
    elif '->' in command:
        u, s = command.split(' -> ')
        for keys, users_list in forceBook.items():
            if u in users_list:
                forceBook[keys].remove(u)
        forceBook = register(s, u, forceBook)
        print(f"{u} joins the {s} side!")

    command = input()

ordered_book = sorted(forceBook.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
for side, users in ordered_book:
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in sorted(users):
            print(f'! {user}')
