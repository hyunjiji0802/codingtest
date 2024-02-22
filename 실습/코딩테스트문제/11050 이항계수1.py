N,K=map(int,input().split())

def 이항계수1(N,K):
    if K<0 or K>N:
        return 0
    else:
        binomial_coefficient=1
        for i in range(N-K+1,N+1):
            binomial_coefficient*=i
        for j in range(2,K+1):
            binomial_coefficient//=j
        return binomial_coefficient
print(이항계수1(N,K))