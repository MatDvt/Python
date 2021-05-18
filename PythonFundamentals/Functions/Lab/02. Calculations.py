def calculations(opr, v1, v2):
    if opr == "multiply":
        return v1 * v2
    elif opr == "divide":
        return v1 // v2
    elif opr == "add":
        return v1 + v2
    elif opr == "subtract":
        return v1 - v2


# 'multiply', 'divide', 'add', 'subtract'
operator = input()
val_1 = int(input())
val_2 = int(input())
result = calculations(operator, val_1, val_2)
print(result)