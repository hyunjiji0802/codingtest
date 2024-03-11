import sys
N=int(sys.stdin.readline().rstrip())
arr=[]
remainder=[]
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

def 검문(arr):
    for i in range(2,max(arr)+1):
        for j in range(N-1):
            if arr[j]%i==arr[j+1]%i:
                if j==N-2:
                    remainder.append(i)
            else:
                break
    print(*remainder)

검문(arr)

