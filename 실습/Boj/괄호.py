import sys

num = int(input())
V=0
for _ in range(num):
    line = sys.stdin.readline().rstrip()

    stack = []
    for i in range(len(line)):
        if line[i] == "(":
            stack.append(line[i])
        else:
            if len(stack) == 0:
                V+=1
            else:
                stack.pop()
                V-=1


    if V<0:
        print("YES")
    else:
        print("NO")
