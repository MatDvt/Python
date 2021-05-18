import re

text = input()

pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"

while not text == "":

    links = [num.group() for num in re.finditer(pattern, text)]
    if links:
        print("/n".join(links))
    text = input()
