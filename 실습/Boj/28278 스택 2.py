import sys

N = int(input())
stack = []
for _ in range(N):
    m = list(map(int, sys.stdin.readline().split()))
    if m[0] == 1:
        stack.append(m[1])
    elif m[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif m[0] == 3:
        print(len(stack))
    elif m[0] == 4:
        print(0 if stack else 1)

    elif m[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)