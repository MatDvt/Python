# •	червено (red)
# •	оранжев (orange)
# •	син (blue)
# •	зелен (green)

eggs_count = int(input())
# egg_color = input()

red_count = 0
orange_count = 0
blue_count = 0
green_count = 0

for egg in range(1, eggs_count + 1):
    egg_color = input()

    if egg_color == 'red':
        red_count += 1
    if egg_color == 'orange':
        orange_count += 1
    if egg_color == 'blue':
        blue_count += 1
    if egg_color == 'green':
        green_count += 1

print(f'Red eggs: {red_count}')
print(f'Orange eggs: {orange_count}')
print(f'Blue eggs: {blue_count}')
print(f'Green eggs: {green_count}')

# the biggest count of colored eggs
if red_count > orange_count and red_count > blue_count and red_count > green_count:
    print(f'Max eggs: {red_count} -> red')
elif orange_count > red_count and orange_count > blue_count and orange_count > green_count:
    print(f'Max eggs: {orange_count} -> orange')
elif blue_count > red_count and blue_count > orange_count and blue_count > green_count:
    print(f'Max eggs: {blue_count} -> blue')
elif green_count > red_count and green_count > orange_count and green_count > blue_count:
    print(f'Max eggs: {green_count} -> green')
