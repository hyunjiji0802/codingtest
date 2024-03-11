a=input()
res=""
for i in range(len(a)):
    if a[i].isupper():
        if ord(a[i])+13 > ord('Z'):
            res+=chr(ord(a[i])+13-26)
        else: res+=chr(ord(a[i])+13)
    elif a[i].islower():
        if ord(a[i]) + 13 > ord('z'):
            res+=chr(ord(a[i]) + 13 - 26)
        else: res += chr(ord(a[i]) + 13)
    else :
        res+=a[i]
print(res)
