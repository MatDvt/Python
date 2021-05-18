#	Дължина в см – цяло число
#	Широчина в см – цяло число
#	Височина в см – цяло число
#	Процент зает обем – реално число

length = int(input())
width = int(input())
height = int(input())
percent = float(input())

percentage = percent * 0.01
aquarium_area = ((length * width * height) * 0.001) * (1 - percentage)

# final_area = aquarium_area * (1-percentage)

print(aquarium_area)
