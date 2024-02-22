import sys

num = int(input())

for _ in range(num):
    line = sys.stdin.readline().rstrip().split()

    for i in line:
        for k in range(len(i), 0, -1):
            print(i[k-1], end='')

        print(end=' ')
