import sys

num=int(input())

deq=[]
front=rear=0

def isEmpty():
    return 1 if len(deq)==0 else 0

for _ in range(num):
    line=sys.stdin.readline().rstrip().split()

    if line[0]=="push_front" :
        deq.insert(0,int(line[1]))
    elif line[0]=="push_back":
        deq.append(int(line[1]))
    elif line[0]=="pop_front":
        if isEmpty()==0:
            print(deq.pop(0))
        else: print(-1)
    elif line[0]=="pop_back":
        if isEmpty()==0:
            print(deq.pop())
        else: print(-1)
    elif line[0]=="size":
        print(len(deq))
    elif line[0]=="empty":
        print(isEmpty())
    elif line[0] == "front":
        if isEmpty()==0:
            print(deq[0])
        else:print(-1)
    elif line[0]=="back":
        if isEmpty()==0:
            print(deq[len(deq)-1])
        else: print(-1)