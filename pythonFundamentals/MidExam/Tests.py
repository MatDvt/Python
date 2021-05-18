a = input()
b = a.split("|")
c = input()


while str(c) != "Done":
    x = c[-1]

    if str(x).isdigit():
        x = int(x)
    if "Move Left" in c:

        if x in range(len(b)):
            b[x], b[x - 1] = b[x - 1], b[x]

        c = input()
    elif "Move Right" in c:

        if x  in range(len(b)):
            b[x + 1], b[x] = b[x], b[x + 1]

        c = input()
    elif "Check Even" in c:
        even_i = []
        for i in range(0, len(b)):
            if i % 2 == 0:
                even_i.append(b[i])
        print(" ".join(even_i))
        c = input()
    elif "Check Odd" in c:
        odd_i = []

        for i in range(0, len(b)):
            if i % 2 != 0:
                odd_i.append(b[i])
        print(" ".join(odd_i))
        c = input()

print("You crafted " + "".join(b) + "!")