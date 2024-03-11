import sys
arr=[]
while True:
    a,b=map(int,sys.stdin.readline().rstrip().split())
    if a==0 and b==0 : break
    arr.append(([a,b]))
b=s=-1
def 배수와약수(case):
        if case[0]>case[1]:
            b=case[0]
            s=case[1]
        else:
            b=case[1]
            s=case[0]
        for i in range(b):
            if b%s==0 and b==case[0]:
                return 'multiple'
            elif b%s==0 and b==case[1]:
                return 'factor'
        return 'neither'

for case in arr:
    print(배수와약수(case))