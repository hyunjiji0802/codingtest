m=[0 for i in range(1001)]

def tiling(n):
    m[1]=1
    m[2]=2
    m[3]=3
    for i in range(4, n+1):
        m[i]=m[i-2]+m[i-1]
    return m[n]
n=int(input())
print(tiling(n)%10007)

def tiling2(n):
    if n<=3: return n

    a=2
    b=3

    for i in range(4,n+1):
        next=a+b
        a=b
        b=next
    return next
print(tiling2(n)%10007)
