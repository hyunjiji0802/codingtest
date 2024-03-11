k=0
dec=0
N, B=input().split()

for i in N:
    if i >="A" and i<="Z" :
        i=ord(i)-55
    else :
        i=int(i)
    dec+=i*(int(B)**(len(N)-1-k))
    k+=1
print(dec)