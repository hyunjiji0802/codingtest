import sys
from collections import deque
n,k = map(int,sys.stdin.readline().rstrip().split(' '))
l = [0 for i in range(100001)] #방문한 숫자 리스트

def bfs(n,k,l):
    t = 0
    deq = deque([(n,t)]) #현재위치랑 현재시간 튜플 담기
    l[n] = 1
    if n>=k:
        return n-k #걸어서 가야함
    while deq:
        # print(deq)
        cur,cur_t = deq.popleft() #큐에서 하나 꺼냄
        if cur == k:  # 같으면 현재 시간 반환
            return cur_t
        # -1 이동
        if  0<= cur-1 <= 100000 and l[cur-1] ==0: #-1 이동 위치에 방문하지 않았고 범위 내에 있다면
            l[cur-1] = 1
            deq.append((cur-1,cur_t+1))
        # +1 이동
        if  0<= cur+1 <= 100000 and l[cur+1] ==0: #+1 이동 위치에 방문하지 않았고 범위 내에 있다면
            l[cur+1] = 1
            deq.append((cur+1,cur_t+1))
        # *2 이동
        if  0<= 2*cur <= 100000 and l[2*cur] ==0: #순간이동 위치에 방문하지 않았고 범위 내에 있다면
            l[2*cur] = 1
            deq.append((2*cur,cur_t+1))
print(bfs(n,k,l))




'''
#재귀 방법
#k를 이동시키면서 n과 만나는지 확인
def find_k(n,k,t):
    print(n,k,t)
    if k<=n: #이미 동생보다 앞에 있으면, 걸어서 뒤로 가기
        return n-k
    if k==1: #동생이 1에 있다면, 수빈이는 1초 후 도착 (재귀 종료 조건)
        return 1
    elif k%2 == 0 : #짝수이면
        return min(find_k(n,k-1,t+1) ,find_k(n,k+1,t+1))+1
    else : #동생의 위치가 홀수이면
        return min(find_k(n,k//2,t+1)+1, k-n)

print(find_k(n,k,t))
'''

