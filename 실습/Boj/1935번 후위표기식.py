import sys

s = []
res = 0
op=[]

n = int(sys.stdin.readline().rstrip())
exp = list(sys.stdin.readline().rstrip())
for _ in range(n):
    op.append(sys.stdin.readline().rstrip())

for i in range(len(exp)):
    if i>len(op): break
    if str(exp[i]).isalpha():
       exp[i]=op.pop(0)

for i in exp:
    print(i)
    if str(i).isdigit():
        s.append(int(i))
    elif i == '+':
        o1=s.pop()
        o2=s.pop()
        res = o2+o1
        s.append(res)
    elif i == '-':
        o1=s.pop()
        o2=s.pop()
        res = o2-o1
        s.append(res)
    elif i == '*':
        o1=s.pop()
        o2=s.pop()
        res = o2*o1
        s.append(res)
    elif i == '/':
        o1=s.pop()
        o2=s.pop()
        res = o2/o1
        s.append(res)

print("%.2f"%res)
