n_wagons = int(input())
wagons = [0] * n_wagons

command = input()

while not command == 'End':
    data = command.split()
    if data[0] == "add":
        people = int(data[1])
        wagons[-1] += people

    elif data[0] == 'insert':
        index = int(data[1])
        people = int(data[2])
        wagons[index] += people

    elif data[0] == 'leave':
        index = int(data[1])
        people = int(data[2])
        wagons[index] -= people
    command = input()
print(wagons)
