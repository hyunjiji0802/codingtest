n = int(input())
i = 0
while True:
    if n == 1: break
    if n % 3 == 0:
        n = n // 3
    elif n % 2 == 0:
        n = n // 2
    else:
        n -= 1
    print(n)
    i += 1

print(i)