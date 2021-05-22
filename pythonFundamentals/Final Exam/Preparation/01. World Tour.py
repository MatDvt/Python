def is_index_valid(index, string):
    if 0 <= index < len(string):
        return True
    return False


initial_string = input()

data = input()

while not data == "Travel":
    command, val_1, val_2 = data.split(":")
    if command.startswith("Add"):
        index = int(val_1)
        if is_index_valid(index, initial_string):
            initial_string = initial_string[:index] + val_2 + initial_string[index:]
    elif command.startswith("Remove"):
        start_index = int(val_1)
        end_index = int(val_2)
        if is_index_valid(start_index, initial_string) and is_index_valid(end_index, initial_string):
            initial_string = initial_string[:start_index] + initial_string[end_index+1:]
    elif command.startswith("Switch"):
        if val_1 in initial_string:
            initial_string = initial_string.replace(val_1, val_2)
    print(initial_string)
    data = input()

print(f"Ready for world tour! Planned stops: {initial_string}")