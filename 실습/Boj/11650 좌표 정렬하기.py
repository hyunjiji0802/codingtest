import sys
input=sys.stdin.readline
N=int(input())
coordinate=[]
for _ in range(N):
    coordinate.append(tuple(map(int, input().split())))

coordinate.sort()
for i in coordinate:
    print(i[0],i[1])