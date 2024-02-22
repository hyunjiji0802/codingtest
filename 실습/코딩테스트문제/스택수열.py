import sys

n = int(sys.stdin.readline().rstrip())

stack = []
op = []
j=0
k=0
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    while n<k:
    stack.append(i+1)
    op.append('+')

if len(stack)==n :
    print("NO")
    print(op)
else:
    for oper in op :
        print(oper)
