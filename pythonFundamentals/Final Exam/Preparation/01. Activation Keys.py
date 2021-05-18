raw = input()
command = input()
while not command == "Generate":
    com = command.split(">>>")
    instruction = com[0]
    if instruction == "Contains":
        sub = com[1]
        if sub in raw:
            print(f"{raw} contains {sub}")
        else:
            print("Substring not found!")
    elif instruction == "Flip":
        ul = com[1]
        start = int(com[2])
        end = int(com[3])
        if ul == "Upper":
            for ch in range(start, end):
                raw[ch].upper()
            print(raw)
        elif ul == "Lower":
            for ch in range(start, end):
                raw[ch].lower()
            print(raw)
    elif instruction == "Slice":
        start = int(com[1])
        end = int(com[2])
        strr = ""
        for ch in range(start, end):
            strr += raw[ch]
        print(raw.replace(strr, ""))
    command = input()
if command == "Generate":
    print(f"Your activation key is: {raw}")
