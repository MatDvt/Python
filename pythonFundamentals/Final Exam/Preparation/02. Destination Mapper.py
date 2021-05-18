import re

pattern = r"(?<=(/|\=))[A-Z][a-zA-Z][a-zA-Z]+(?=\1)"
text = input()

valid_destinations = [dest.group() for dest in re.finditer(pattern, text)]

travel_points = sum([len(d)for d in valid_destinations])
print(f"Destinations: {', '.join(valid_destinations) }")
print(f"Travel Points: {travel_points}")