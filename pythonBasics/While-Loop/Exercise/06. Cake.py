width = int(input())
length = int(input())

sum_of_pieces = width * length  # the whole cake

piece = input()
while piece != 'STOP':
    sum_of_pieces -= int(piece)
    if sum_of_pieces < 1:
        break
    piece = input()

if sum_of_pieces >= 1:
    print(f'{sum_of_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(sum_of_pieces)} pieces more.')
# print(f'{abs(cake_area - sum_of_pieces)} pieces are left.')


# print(f'No more cake left! You need {abs(cake_area - sum_of_pieces)} pieces more."')
