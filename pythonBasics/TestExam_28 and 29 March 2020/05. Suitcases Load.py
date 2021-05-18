capacity = float(input())
command = input()

counter = 0
is_space = True

while command != "End":
    number = float(command)
    if capacity <= number:
        is_space = False
        break

    capacity -= number
    counter += 1

    if counter % 3 == 0:
        capacity -= number * 0.10
        if capacity < 0:
            is_space = False
            counter -= 1
            break

    command = input()

if not is_space:
    print("No more space!")

if is_space:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {counter} suitcases loaded.")
