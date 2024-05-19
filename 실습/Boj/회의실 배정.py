import sys
n = int(sys.stdin.readline().rstrip())
m = [tuple(map(int,sys.stdin.readline().split())) for i in range(n)]
m.sort(key=lambda x:(x[0],x[1]-x[0]))
# print(m)
answer = [m[0]]
#전체 회의 구간
t = max(list(zip(*m))[1]) - min(list(zip(*m)))[0]
#전체 회의 가능한 시간대 내에서, 남은 회의 시간이 최대가 되어야 함 -> 가장 짧은 회의들 먼저 넣기

for i in range(1,n):
    if answer[-1][1] > m[i][0]: #회의 시간 겹치면
        if answer[-1][1] > m[i][1]: #먼저 끝나면
            answer.pop() #answer pop & 선택할 회의 append
            answer.append(m[i])
        else: #먼저 끝나지 않는 경우
            if t - answer[-1][1] < t - m[i][1]: # 먼저 있는 회의 vs 선택할 회의 둘 중 r_time이 최대가 되도록 하는 회의 고르기
                answer.pop() #answer pop & 선택할 회의 append
                answer.append(m[i])
    else: #안겹치면 일단 answer에 append
        answer.append(m[i])
print(len(answer))
print(answer)