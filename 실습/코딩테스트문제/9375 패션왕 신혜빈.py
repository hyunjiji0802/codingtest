import sys
from itertools import combinations

N=int(input())
arr=[]
print(arr)
for i in range(N):
    K=int(input())
    list=[]
    for j in range(K):

        list.append(tuple(sys.stdin.readline().rstrip().split()))
    arr.append(list)
print(arr)