import sys
n=int(input())
s=[]

for i in range(n):
    s.append(list(map(int,sys.stdin.readline().rstrip().split())))

k=2

for i in range(1,n):
    for j in range(k):
        if j==0:
            s[i][j]=s[i][j]+s[i-1][j]
        elif i==j:
            s[i][j] = s[i][j] + s[i - 1][j-1]
        else:
            s[i][j]=max(s[i-1][j-1]+s[i][j], s[i-1][j]+s[i][j])

    k+=1
print(max(s[n-1]))
