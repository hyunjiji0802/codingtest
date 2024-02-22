a=input()
b=[-1 for i in range(26)]
for i in range(len(a)):
    for k in range(0,26):
        if ord(a[i])-97==k:
            if b[k] == -1:
                b[k]=i

for k in b:
    print(k, end=' ')
