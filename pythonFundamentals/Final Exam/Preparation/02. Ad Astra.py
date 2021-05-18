import re

text = input()
pattern = r"(#|\|)(?P<item>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>([0-9][0-9]{0,3}|10000))\1"

total_calories = 0

matches = [data.groupdict() for data in re.finditer(pattern, text)]

for index in range(len(matches)):
    total_calories += int(matches[index]["calories"])

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")
for index in range(len(matches)):
    print(f"Item: {matches[index]['item']}, Best before: {matches[index]['date']}, Nutrition: {matches[index]['calories']}")
