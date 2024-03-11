n=int(input())
card=list(map(int,input().split()))
card.insert(0,0)
mincost=[0]+[10001]*n

for i in range(1,n+1):
    for k in range(1,i+1):

        mincost[i]=min(card[k]+mincost[i-k], mincost[i])
print(mincost[i])