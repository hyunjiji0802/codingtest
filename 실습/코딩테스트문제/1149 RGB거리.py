import sys
n=int(input())
s=[]
for i in range(n):
    s.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1,n):
    s[i][0] = min(s[i-1][1] + s[i][0], s[i-1][2] + s[i][0])
    s[i][1] = min(s[i-1][0] + s[i][1], s[i-1][2] + s[i][1])
    s[i][2] = min(s[i-1][0] +s[i][2], s[i-1][1] +s[i][2])

print(min(s[n-1][0],s[n-1][1],s[n-1][2]))

