import re

text = input()
searched_word = input()

pattern = rf"\b{searched_word}\b"
word_occurance = re.findall(pattern, text, re.IGNORECASE)
print(len(word_occurance))