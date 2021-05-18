data = input().split(" -> ")
company_users = {}

while not data[0] == "End":
    company = data[0]
    employee_id = data[1]

    if company not in company_users:
        company_users[company] = [employee_id]
    else:
        if employee_id not in company_users[company]:
            company_users[company].append(employee_id)

    data = input().split(" -> ")

sorted_company = sorted(company_users.items(), key=lambda kvp: kvp[0], reverse=False)

for key, value in sorted_company:
    print(f"{key}")
    sorted_value = sorted(value)
    for val in value:
        print(f"-- {val}")
