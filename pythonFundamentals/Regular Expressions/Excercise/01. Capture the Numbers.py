import re

data = input()
all_nums = []
pattern = r"[0-9]+"  # an alternative would be \d+

while not data == "":
    valid_numbers = re.findall(pattern, data)
    all_nums.extend(valid_numbers)  #list.extend
    data = input()
print(*all_nums)
