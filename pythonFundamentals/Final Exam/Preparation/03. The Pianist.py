n = int(input())
pieces = {}


for _ in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {'composer': composer, 'key': key}


data = input()

while not data == "Stop":
    command = data.split("|")
    if command[0] == "Add":
        piece, composer, key = command[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece, new_key = command[1:]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    data = input()

sorted_pieces = sorted(pieces.items(), key=lambda tkvp: (tkvp[0], tkvp[1]['composer']))
for piece, data in sorted_pieces:
    print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")