import re

data = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

valid_numbers = [match_obj.group() for match_obj in re.finditer(pattern, data)]
print(" ".join(valid_numbers))
print(*valid_numbers)  # unpack the values directly instead of using string .join
