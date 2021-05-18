#Write a program which reads numbers from the console until it receives a number between 1 and 100 inclusive.
# #When the correct number is received, stop reading and print "The number {number} is between 1 and 100"

number = float(input())

while number < 1 or number > 100:
    number = float(input())
print(f'The number {number} is between 1 and 100')