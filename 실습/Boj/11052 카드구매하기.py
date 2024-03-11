n=int(input())
card=list(map(int,input().split()))
card.insert(0,0)
maxcost=[0]*(n+1)
maxcost[1]=card[1]
for i in range(1,n+1):
    for k in range(1,i+1):
        print(maxcost)
        maxcost[i]=max(card[k]+maxcost[i-k], maxcost[i])

print(maxcost[i])


'''
for i in range(1,n+1):
    for k in range(1,i+1):
        print(maxcost)
        maxcost[i] = max(maxcost[i], maxcost[i-k] + card[k])
print(maxcost[i])


'''