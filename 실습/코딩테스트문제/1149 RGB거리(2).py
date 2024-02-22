import sys
N=int(input())
s=[]
arr=[0]*(N+1)
for i in range(N):
    s.append(list(map(int, sys.stdin.readline().rstrip().split())))

def RGB거리(N):
    for i in range(1,N):
        for k in range(3):
            if k==0:
                s[i][k] = min(s[i][k] + s[i - 1][1], s[i][k] + s[i - 1][2])
            elif k == 1:
                s[i][k] = min(s[i][k] + s[i - 1][0], s[i][k] + s[i - 1][2])
            else:
                s[i][k] = min(s[i][k] + s[i - 1][0], s[i][k] + s[i - 1][1])

    print(min(s[-1]))
RGB거리(N)
