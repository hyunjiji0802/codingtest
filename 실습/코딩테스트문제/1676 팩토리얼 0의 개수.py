n=int(input())
s=0
i=-1
def pactorial(n):
    if n==0:
        return 1
    else:
        return n*pactorial(n-1)

pac=pactorial(n)
pac=list(str(pac))
while True:
    if pac[i]=='0':
        s+=1
        i-=1
    else:
        break

print(s)