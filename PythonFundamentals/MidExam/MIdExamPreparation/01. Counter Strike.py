initial_energy = int(input())

distance = input()
counter_wins = 0
is_won = True

while not distance == "End of battle":
    distance = int(distance)

    if initial_energy - distance >= 0:
        initial_energy -= distance
        counter_wins += 1
        if counter_wins % 3 == 0:
            initial_energy += counter_wins
    else:
        is_won = False
        print(f'Not enough energy! Game ends with {counter_wins} won battles and {initial_energy} energy')
        break

    distance = input()

if is_won:
    print(f'Won battles: {counter_wins}. Energy left: {initial_energy}')
