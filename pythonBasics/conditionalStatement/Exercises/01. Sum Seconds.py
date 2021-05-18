import math

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third  # sumirane na secundite

minutes = total_time / 60  # prevrashteme v minutes
seconds = total_time % 60  # calculating the seconds

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
