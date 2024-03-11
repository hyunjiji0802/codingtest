s=input()
a=[]
for i in range(len(s)):
    a.append(s[i:len(s)])
a.sort()

for k in a:
    print(k)
