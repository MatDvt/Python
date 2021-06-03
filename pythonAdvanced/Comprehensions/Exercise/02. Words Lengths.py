text = [word for word in input().split(", ")]

output = [f'{word} -> {len(word)}'for word in text]
print(', '.join(output))



