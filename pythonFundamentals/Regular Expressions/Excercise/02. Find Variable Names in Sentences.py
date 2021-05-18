import re

data = input()

pattern = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"

valid_ids = [num.group() for num in re.finditer(pattern, data)]
print(",".join(valid_ids))
