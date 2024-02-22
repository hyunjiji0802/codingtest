import sys

T=int(sys.stdin.readline().rstrip())
s=[]
zero=[1,0,1]+[0]*38
one=[0,1,1]+[0]*38

for _ in range(T):
    s.append(int(sys.stdin.readline().rstrip()))

def fibo():
    for i in range(3,41):
        zero[i]=zero[i-2]+zero[i-1]
        one[i]=one[i-2]+one[i-1]
fibo()
for i in range(T):
    print(zero[s[i]], one[s[i]])

