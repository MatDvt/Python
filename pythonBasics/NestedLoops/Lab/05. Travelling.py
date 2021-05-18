destination = input()

while destination != 'End':
    min_budget = float(input())
    sum = 0
    while sum < min_budget:
        saved_money = float(input())
        sum += saved_money
    else:
        print(f'Going to {destination}!')

    destination = input()

destination = input()

# спираме destination == "End"
while destination != "End":
    min_budget = float(input())
    # спира да събира: парите >= мин.бюджет
    sum = 0
    while sum < min_budget:
        saved_money = float(input())
        sum += saved_money
    else:
        print(f"Going to {destination}!")

    destination = input()
