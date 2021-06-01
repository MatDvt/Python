# one way with queue

from collections import deque

rows, cols = map(int, input().split())
snake = deque(input())
mx = []

for y in range(rows):
    for x in range(cols):
        snake.append(snake.popleft())
        if y % 2 == 0:
            mx.append(snake[-1])
        else:
            mx.insert(0, snake[-1])
    print(''.join(mx))
    mx = []
