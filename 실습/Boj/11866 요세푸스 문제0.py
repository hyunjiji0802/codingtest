from collections import deque
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
queue = deque()
for i in range(N):
    queue.append(i+1)
print('<', end='')
while len(queue) > 1:
    queue.rotate(-(K-1))
    print(queue.popleft(), end=', ')

print(queue[0],'>', sep='')