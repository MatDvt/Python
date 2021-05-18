capacity = int(input())

message_dict = {}

while True:
    command = input()
    if command == 'Statistics':
        break
    args = command.split('=')
    action = args[0]
    if action == 'Add':
        name = args[1]
        sent = int(args[2])
        received = int(args[3])
        if name not in message_dict.keys():
            message_dict[name] = [0, 0]
            message_dict[name][0] = sent
            message_dict[name][1] = received
    elif action == 'Message':
        sender = args[1]
        receiver = args[2]
        if sender in message_dict.keys() and receiver in message_dict.keys():
            message_dict[sender][0] += 1
            message_dict[receiver][1] += 1
            if message_dict[sender][0] + message_dict[sender][1] == capacity:
                del message_dict[sender]
                print(f"{sender} reached the capacity!")
            if message_dict[receiver][0] + message_dict[receiver][1] == capacity:
                del message_dict[receiver]
                print(f"{receiver} reached the capacity!")
    elif action == 'Empty':
        if args[1] == 'All':
            message_dict.clear()
        else:
            name = args[1]
            del message_dict[name]

print(f'Users count: {len(message_dict)}')

message_dict = dict(sorted(message_dict.items(), key=lambda x: (-x[1][1], x[0])))

for (key, value) in message_dict.items():
    print(f'{key} - {sum(value)}')