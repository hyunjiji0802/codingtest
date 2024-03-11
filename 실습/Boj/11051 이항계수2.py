N,K=map(int,input().split())
pascal=[]

def 이항계수2(N,K):
    for i in range(N+1):
        pascal.append([1]*(i+1))

    for i in range(2,N+1):
        for j in range(1, i):
            pascal[i][j]=(pascal[i-1][j-1]+pascal[i-1][j])%10007

    return pascal[N][K]

print(이항계수2(N,K)%10007)