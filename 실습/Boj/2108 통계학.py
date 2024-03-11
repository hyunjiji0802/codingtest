import sys
from collections import Counter
input=sys.stdin.readline
N=int(input())
arr=[]
for _ in range(N):
    arr.append(int(input()))

def 통계학(arr):
    arr.sort()
    산술평균=0
    freq=Counter(arr).most_common()
    maximum=freq[0][1]

    mode=[]
    for i in freq:
        if i[1]==maximum:
            mode.append(i[0])

    for i in range(N):
        산술평균+=arr[i]

    산술평균=round(산술평균/N)
    중앙값=arr[N//2]
    최빈값=mode[1] if len(mode)>1 else mode[0]
    범위=arr[-1]-arr[0]

    print(산술평균, 중앙값, 최빈값, 범위)
통계학(arr)
