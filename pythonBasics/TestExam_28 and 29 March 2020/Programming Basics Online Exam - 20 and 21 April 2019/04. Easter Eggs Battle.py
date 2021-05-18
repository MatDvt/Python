eggs_player_1 = int(input())
eggs_player_2 = int(input())

command = input()
while command != 'End of battle':
    if command == 'one':
        eggs_player_2 -= 1
    if command == 'two':
        eggs_player_1 -= 1
    if eggs_player_1 == 0:
        print(f'Player one is out of eggs. Player two has {eggs_player_2} eggs left.')
        break
    if eggs_player_2 == 0:
        print(f'Player two is out of eggs. Player one has {eggs_player_1} eggs left.')
        break

    command = input()

if command == 'End of battle':
    print(f'Player one has {eggs_player_1} eggs left.')
    print(f'Player two has {eggs_player_2} eggs left.')
