from itertools import combinations

N, M=list(map(int, input().split()))
Card=list(map(int, input().split()))
Comb=list(combinations(Card, 3))
def BlackJack(Comb, M):
    max=0
    for i in Comb:
        sum=0
        for j in range(3):
            sum+=i[j]
        if sum<=M and sum>max:
            max=sum
    return max

print(BlackJack(Comb,M))