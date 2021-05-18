text = input()

emojis = [f"{text[symbol]}{text[symbol + 1]}" for symbol in range(0, len(text)) if text[symbol] == ":"]

print("\n".join(emojis))
