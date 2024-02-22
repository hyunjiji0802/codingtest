import sys
sys.setrecursionlimit(10**5)
n,m=map(int,input().split())
s=0
i=-1
def pactorial(n):
    if n == 0:
        return 1
    else:
        return n * pactorial(n - 1)

comb= int(pactorial(n)/pactorial(m)/pactorial(n-m))
comb=list(str(comb))
while True:
    if comb[i]=='0':
        s+=1
        i-=1
    else:
        break
print(s)