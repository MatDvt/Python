username = input()
password = input()

data = ''
while data != password:
    data = input()
print(f'Welcome {username}!')
