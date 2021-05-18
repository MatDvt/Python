#Write a program that receives a single integer number and prints different messages depending on the number:
#	If Oscar is 88 - "Leo finally won the Oscar! Leo is happy".
#	If Oscar is 86 - "Not even for Wolf of Wall Street?!"
#	If Oscar is not 88 nor 86 (and below 88) - "When will you give Leo an Oscar?"
#	If Oscar is over 88 - "Leo got one already!"

var = int(input())

if var is not 88 and var is not 86 and var < 88:
    print(f'When will you give Leo an Oscar?')
elif var == 88:
    print(f'Leo finally won the Oscar! Leo is happy')
elif var == 86:
    print(f'Not even for Wolf of Wall Street?!')
else:
    print(f'Leo got one already!')


