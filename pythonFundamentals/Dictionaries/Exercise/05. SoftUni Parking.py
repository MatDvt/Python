n_commands = int(input())
dct_all_cars = {}

for n in range(n_commands):
    data = input().split()
    command = data[0]
    user = data[1]

    if command == "register":
        license_plate = data[2]
        if user not in dct_all_cars:
            dct_all_cars[user] = license_plate
            print(f"{user} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif command == "unregister":
        if user not in dct_all_cars:
            print(f"ERROR: user {user} not found")
        else:
            dct_all_cars.pop(user)
            print(f"{user} unregistered successfully")
for key, value in dct_all_cars.items():
    print(f"{key} => {value}")
