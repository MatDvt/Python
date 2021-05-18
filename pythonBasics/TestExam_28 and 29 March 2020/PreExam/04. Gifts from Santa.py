# От конзолата се четат точно 3 числа, всяко на отделен ред:
# •	N – цяло число – 0 <= N < M
# •	M – цяло число – N < M <= 10000
# •	S – цяло числo – N <= S <= M

n = int(input())
m = int(input())
s = int(input())

for num in range(m, n, - 1):
    if num % 2 == 0 and num % 3 == 0:

        if s == num:
            break
        print(num, end=' ')
