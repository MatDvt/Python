n_snowballs = int(input())

max_snowball_value = -999999999999999

for _ in range(n_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality