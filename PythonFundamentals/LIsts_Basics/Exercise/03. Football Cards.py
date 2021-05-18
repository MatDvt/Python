cards = input()

c_list = cards.split()
no_duplicate = []
team_A = 11
team_B = 11
terminated = False

l_team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
l_team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

for i in c_list:
    if i not in no_duplicate:
        no_duplicate.append(i)

for element in no_duplicate:
    if element in l_team_a:
        team_A -= 1
    if element in l_team_b:
        team_B -= 1
    if team_A < 7 or team_B < 7:
        terminated = True
        break

print(f'Team A - {team_A}; Team B - {team_B}')
if terminated is True:
    print(f'Game was terminated')
