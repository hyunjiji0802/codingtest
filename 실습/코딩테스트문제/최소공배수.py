import sys

def gcd(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m%n == 0:
        return n
    else:
        return gcd(n, m%n)

num=int(sys.stdin.readline().rstrip())
for i in range(int(num)):
    s=list(map(int,sys.stdin.readline().rstrip().split()))
    x=gcd(s[0],s[1])

    lcm=int(s[0]*s[1]/x)
    print(lcm)
