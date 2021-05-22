encrypted_message = input()

data = input()


# TODO refactor the code in ifs to use functions

while not data == "Decode":
    command = data.split("|")
    if command[0] == "ChangeAll":
        replace = command[1]
        replace_with = command[2]
        encrypted_message = encrypted_message.replace(replace, replace_with)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        first_part = encrypted_message[:index]
        second_part = encrypted_message[index:]
        encrypted_message = first_part + value + second_part
    elif command[0] == "Move":
        n_chars = int(command[1])
        chars_to_move = encrypted_message[:n_chars]
        first_part = encrypted_message[n_chars:]
        encrypted_message = first_part + chars_to_move
    data = input()

print(f"The decrypted message is: {encrypted_message}")