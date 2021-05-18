deposit_sum = float(input())
months = int(input())
percentage = float(input())

earnings = deposit_sum + months * ((deposit_sum * percentage / 100) / 12)

print(earnings)
