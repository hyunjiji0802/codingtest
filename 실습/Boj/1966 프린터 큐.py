from collections import deque
import sys

Num = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(Num):

    N, M = map(int, sys.stdin.readline().rstrip().split())
    queue=deque(map(int,sys.stdin.readline().rstrip().split()))
    order = deque(i for i in range(N))

    num=queue[M]
    id=0
    while len(queue)>0:
        if max(queue) != queue[0]:
            queue.rotate(-1)
            order.rotate(-1)
        else:
            id+=1
            od = order.popleft()
            pop = queue.popleft()
            if pop == num and od == M :
                print(id)
                break

    queue.clear()
