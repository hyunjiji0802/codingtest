import sys
T=int(sys.stdin.readline().rstrip())
arr=[]
pascal=[]

for _ in range(T):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(31):
    pascal.append([1]*(i+1))

for i in range(2,31):
    for j in range(1, i):
        pascal[i][j]=(pascal[i-1][j-1]+pascal[i-1][j])

for i in range(T):
    print(pascal[arr[i][1]][arr[i][0]])