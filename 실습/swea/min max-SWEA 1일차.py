T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print("#%d %d"%(i+1,max(arr)-min(arr)))