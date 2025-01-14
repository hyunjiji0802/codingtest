a=[1,2,3]
b=a.copy()
print(a[1:2])
a[1:2] = [4,5]
print(a,b)
print(a[1:2])
