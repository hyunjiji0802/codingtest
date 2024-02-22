import sys
num=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
print(min(arr)*max(arr))
