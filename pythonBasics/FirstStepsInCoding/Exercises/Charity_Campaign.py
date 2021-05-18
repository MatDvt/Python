days = int(input())
confectioner = int(input())
cakes = int(input()) * 45
bagels = int(input()) * 5.8
pancakes = int(input()) * 3.2

sum = ((cakes + bagels + pancakes) * confectioner) * days
expenses = (sum * 0.125)
print(sum - expenses)
