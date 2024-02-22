import sys
N=int(sys.stdin.readline().rstrip())

def 분해합(N):
    M=N-1
    arr=[0,]
    while M>0:
        sum=div=M
        while div>0:
            sum+=div%10
            div//=10

        if sum==N:
            arr.append(M)
        M-=1

    return arr[-1]

print(분해합(N))