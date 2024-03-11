N=int(input())
arr=[0]*(N+2)
arr[1]=1
arr[2]=2
def 타일(N):
    if N<=2:
        return arr[N]
    for i in range(3,N+1):
        arr[i]=(arr[i-2]+arr[i-1])%15746
    return arr[N]
print(타일(N))