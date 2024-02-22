import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
l=deque()

for _ in range(N):
    l.append(list(map(int,sys.stdin.readline().rstrip().split())))
for j in range(N):
    print(l[j])

def 색종이(N):
    for i in range(N):
        if