n=int(input())
dp=[[0] *10 for i in range(n)]
dp[0]=[1 for i in range(10)]

for i in range(1,n):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
    print(dp)
if n==1 :
    print(10)
else:
    print(sum(dp[n-1])%10007)