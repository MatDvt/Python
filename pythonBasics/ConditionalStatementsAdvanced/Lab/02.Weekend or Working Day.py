day = input()

if day != 'Monday' and day != 'Tuesday' and day != 'Wednesday' and day != 'Thursday' and day != 'Friday' and day != 'Saturday' and day != 'Sunday':
    print('Error')

if day == 'Monday':
    print('Working day')
elif day == 'Tuesday':
    print('Working day')
elif day == 'Wednesday':
    print('Working day')
elif day == 'Thursday':
    print('Working day')
elif day == 'Friday':
    print('Working day')
elif day == 'Saturday':
    print('Weekend')
elif day == 'Sunday':
    print('Weekend')
