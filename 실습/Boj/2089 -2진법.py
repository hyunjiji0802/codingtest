N=int(input())
s=[]
if N==0: exit()
while True:
    if N==1:
        break
    i=N%(-2)
    print(N//(-2))
    s.insert(0,i)
    print(i)
print(s)