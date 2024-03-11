from collections import deque
import sys
K=int(sys.stdin.readline().rstrip())
d=deque()
for _ in range(K):
    num=int(sys.stdin.readline().rstrip())
    if num == 0:
        d.pop()
    else:
        d.append(num)
sum=0
for n in d:
    sum+=n
print(sum)