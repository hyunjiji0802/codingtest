n=int(input())
s=list(map(int, range(0,int(n**0.5)+1)))
count=[0]*n
print(s)
for i in range(int(n**0.5),0,-1):
    for k in range(i,0,-1):
        if i**2 + k**2==n :
            count[1]+=2
        elif i**2 + k**2 <n:
            n-=i**2-k**2
            count[1]+=1
        else :


        print(s[k])
        print(s[i])
    print("    --------    ")
    n = n - int(n ** 0.5)