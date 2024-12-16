from collections import deque
def issame(A,N):
    for i in range(N):
        if i== N-1:
            continue
        if A[i]!=A[i+1]:
            return False
    return True

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    A = deque(map(int,input().split()))
    answer = 0
    before = set()

    first_A = A.copy()
    while True:
        if issame(A,N):
            print("#%d" % (tc), answer)
            break

        cur = tuple(A)
        if cur in before:
            print("#%d" % (tc), -1)
            break
        before.add(cur)

        A.append(A[K-1])
        A.popleft()
        answer +=1


# 3
# 4 2
# 1 5 5 3
# 4 1
# 3 3 3 3
# 4 3
# 2 3 4 4
