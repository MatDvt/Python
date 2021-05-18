goal_steps = 10000
steps_sum = 0

while steps_sum < goal_steps:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        steps_sum += steps
        break
    steps_sum += int(steps)

diff = abs(steps_sum - goal_steps)
if steps_sum >= goal_steps:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')
