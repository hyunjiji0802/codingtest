m=[0 for i in range(1001)]

def tiling(n):
    m[1]=1
    m[2]=3
    m[3]=5
    for i in range(4, n+1):
        m[i]=2*m[i-2]+m[i-1]
    return m[n]
n=int(input())
print(tiling(n)%10007)

def tiling2(n):
    a=1
    b=3

    for i in range(3,n+1):
        next=2*a+b
        a=b
        b=next
    return next
print(tiling2(n)%10007)
