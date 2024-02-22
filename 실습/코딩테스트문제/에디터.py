import sys

left = list(sys.stdin.readline().rstrip())
num = int(sys.stdin.readline().rstrip())

right=[]
for _ in range(num):
    line = sys.stdin.readline().rstrip().split()

    if line[0] == "L" and len(left)!= 0:
        right.append(left.pop())
    elif line[0] == "D" and len(right)!= 0:
        left.append(right.pop())
    elif line[0] == "B" and len(left)!=0:
        left.pop()
    elif line[0] == "P":
        left.append(line[1])

right.reverse()
left=left+right
for i in left:
    print(i, end='')

