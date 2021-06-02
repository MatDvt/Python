text = [word for word in input().split(", ")]

print(f"{' '.join(text,)} -> {[len(word)for word in text]}")