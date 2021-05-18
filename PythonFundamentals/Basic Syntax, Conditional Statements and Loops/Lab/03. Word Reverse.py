# Write a program that receives a single word from the user, reverses it and prints it

word = input()

# using .join
#print(''.join(reversed(word)))

# using a for loop
reversed_word = ''
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print(reversed_word)

# using Slicing:

#print(word[:: -1])
