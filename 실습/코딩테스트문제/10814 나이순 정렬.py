import sys
N=int(input())
arr=[]
for i in range(N):
    age, name=sys.stdin.readline().rstrip().split()
    arr.append(tuple([int(age),name,i]))

arr.sort(key=lambda x:(x[0],x[2]))

for i in arr:
    print(i[0], i[1])