import sys

number = int(input())
line = [0 for i in range(number)]
for i in range(number):
    line[i] = int(sys.stdin.readline().rstrip())

def P(n):
    if n <= 2: return n
    if n == 3: return 4
    a = 1
    b = 2
    c = 4

    for i in range(3, n):
        temp = a + b + c
        a = b
        b = c
        c = temp
    return temp


for i in line:
    print(P(i))