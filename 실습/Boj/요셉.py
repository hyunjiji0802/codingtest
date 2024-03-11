import sys
line=input().split()
n=int(line[0])
k=int(line[1])

i=k-1
num=n
seq=list(range(1,n+1))

p=[]

print("<", end='')
for _ in range(n):
    p.append(seq.pop(i))
    i+=k-1
    num-=1
    if i>=num and num!=0:
        i=i%num

for i in range(n):
    if i==n-1:
        print(p[i], end=">")
    else : print(p[i], end=', ')