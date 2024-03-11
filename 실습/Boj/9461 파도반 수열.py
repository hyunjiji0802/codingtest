import sys
T=int(sys.stdin.readline().rstrip())
s=[]
for _ in range(T):
    s.append(int(sys.stdin.readline().rstrip()))
arr=[0,1,1,1,2,2]+[0]*95
def P():
    for i in range(6,101):
        arr[i]=arr[i-1]+arr[i-5]
    return arr
P()
for i in range(T):
    print(arr[s[i]])