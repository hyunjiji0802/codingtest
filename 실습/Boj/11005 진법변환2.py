N, B=map(int,input().split())
s=[]
while True:
    a=N%B
    if a>9:
        a=chr(a+55)
    else:
        a=int(a)
    s.insert(0,a)
    if N<B: break
    N=int(N/B)

print("".join(map(str, s)))
