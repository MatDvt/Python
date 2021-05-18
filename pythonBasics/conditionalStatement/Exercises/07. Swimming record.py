record = float(input())
distance = float(input())
time = float(input())

result = distance * time
delay = (distance // 15) * 12.5  # namirane na vremeto samo za zabavqne
result += delay

if result < record:
    print(f'Yes, he succeeded! The new world record is {result:.2f} seconds.')
else:
    print(f'No, he failed! He was {result - record:.2f} seconds slower.')
