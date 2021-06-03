countries = input().split(", ")
capitals = input().split(", ")

dict = {country: capital for country, capital in zip(countries, capitals)}

print('\n'.join([f'{country} -> {city}' for country, city in dict.items()]))
