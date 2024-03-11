import sys
N=int(sys.stdin.readline().rstrip())
arr=list(map(int, sys.stdin.readline().rstrip().split()))

def gcd(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m%n == 0:
        return n
    else:
        return gcd(n, m%n)

def 링(arr):
    R=arr[0]
    for i in range(1,N):
        M=gcd(R,arr[i])
        print('%d/%d' %(R//M, arr[i]//M))

링(arr)