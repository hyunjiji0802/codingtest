import sys
n=int(input())

dp=[0 for i in range(n+1)]
for i in range(1,n+1):
    dp[i]=int(sys.stdin.readline().rstrip())

for i in range(1,n+1):
    for j in range(1,i):
        if 
            dp[i]=max(dp[j]+dp[j-1], dp[i])
    print(dp)

print(dp)
print(max(dp))
