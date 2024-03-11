import sys
n=int(input())
s=list(map(int,sys.stdin.readline().rstrip().split()))
sum=[s[0]]
for i in range(len(s)-1):
        sum.append(max(sum[i]+s[i+1], s[i+1]))
if max(sum)<-max(s):
    print(-max(s))