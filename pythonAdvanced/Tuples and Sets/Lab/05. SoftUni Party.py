num = int(input())

reservations = set()
for ticket in range(num):
    ticket = input()
    reservations.add(ticket)

guest = input()
while not guest == "END":
    reservations.remove(guest)
    guest = input()

print(len(reservations))
for guest in sorted(reservations):
    if guest[0].isdigit():
        print(guest)

for guest in sorted(reservations):
    if guest[0].isalpha():
        print(guest)