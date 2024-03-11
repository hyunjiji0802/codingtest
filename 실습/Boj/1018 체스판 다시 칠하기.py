import sys
N,M=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for _ in range(N):
    arr.append(list(sys.stdin.readline().rstrip()))
def 체스판(arr,N,M):
    mincnt=64
    for i in range(N-7):
        for j in range(M-7):
            cnt = 0
            for k in range(i,i+8):
                for m in range(j,j+8):
                    if m%2==0 and k%2==0 and arr[k][m]!="W":
                        cnt+=1
                    if m%2!=0 and k%2==0 and arr[k][m]!="B":
                        cnt+=1
                    if m%2!=0 and k%2!=0 and arr[k][m]!="W":
                        cnt+=1
                    if m%2==0 and k%2!=0 and arr[k][m]!="B":
                        cnt+=1
            cnt=cnt if cnt<64-cnt else 64-cnt
            if cnt<mincnt:
                mincnt=cnt

    return mincnt

print(체스판(arr,N,M))