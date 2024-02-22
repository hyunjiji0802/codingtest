import sys
input=sys.stdin.readline().rstrip
N=str(input())
arr=list(map(int,N))
arr.sort()
arr.reverse()

print("".join(map(str,arr)))