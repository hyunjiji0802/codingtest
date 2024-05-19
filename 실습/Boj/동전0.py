import sys
n,k = map(int,sys.stdin.readline().rstrip().split())
k_list = [int(sys.stdin.readline().rstrip())  for i in range(n)]
k_list.reverse()
answer = 0
for i in range(n):
    if k_list[i] <= k: #동전 처리 할 수 있으면
        answer += k//k_list[i] #나머지와 몫으로 연산 속도 줄여야 시간초과X
        k = k%k_list[i]
        # print(k)

print(answer)