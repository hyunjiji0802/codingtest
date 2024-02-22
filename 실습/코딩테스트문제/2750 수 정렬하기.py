import sys
N=int(sys.stdin.readline().rstrip())
arr=[]
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()

for i in arr:
    print(i)