# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# •	Първият ред съдържа час на изпита – цяло число от 0 до 23;
# •	Вторият ред съдържа минута на изпита – цяло число от 0 до 59;
# •	Третият ред съдържа час на пристигане – цяло число от 0 до 23;
# •	Четвъртият ред съдържа минута на пристигане – цяло число от 0 до 59.

exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

# converting the hours in minutes and adding them to the minutes variable so we can have one variable that holds the mins and hours
exam_time = exam_hour * 60 + exam_min
arrival_time = arrival_hour * 60 + arrival_min
diff = arrival_time - exam_time

# hh:mm hours before the start
hh = abs(diff) // 60
mm = abs(diff) % 60

if diff < -30:
    print('Early')
    if hh > 0:
        print(f'{hh}:{mm:02d} hours before the start')
    else:
        print(f'{mm} minutes before the start')
elif diff <= 0:
    print('On time')
    if not diff == 0:
        if hh > 0:
            print(f'{hh}:{mm:02d} hours before the start')
        else:
            print(f'{mm} minutes before the start')
else:
    print('Late')
    if hh > 0:
        print(f'{hh}:{mm:02d} hours after the start')
    else:
        print(f'{mm} minutes after the start')
