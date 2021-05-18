all_words = [word for word in input().split() if word == word[::-1]]
searched = input()

print(all_words)
print(f'Found palindrome {all_words.count(searched)} times')
