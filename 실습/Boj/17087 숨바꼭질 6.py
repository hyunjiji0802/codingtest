import sys
n, s=map(int,input().split())
nlist=list(map(int, sys.stdin.readline().rstrip().split()))

k=0

def gcd(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m%n == 0:
        return n
    else:
        return gcd(n, m%n)
for i in range(len(nlist)):
    if nlist[i]<=s:
        nlist[i]=s-nlist[i]
    else :
        nlist[i]=nlist[i]-s
g=max(nlist)
while k<n-1 :

    if k==0:
        g=gcd(nlist[k],nlist[k+1])
    else :
        g=gcd(g,nlist[k+1])
    k+=1

print(g)

