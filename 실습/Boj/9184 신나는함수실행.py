import sys
a=b=c=-51
arr=[]
while True:
    a,b,c=list(map(int,sys.stdin.readline().rstrip().split()))
    if a==b==c==-1:
        break
    arr.append([a,b,c])

def w(a,b,c):

print(arr)