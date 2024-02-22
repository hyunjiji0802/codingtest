import sys

num = int(sys.stdin.readline().rstrip())
queue = []
bottom = 0
top = 0


def push(n):
    queue.append(n)


def pop():
    if empty() != 1:
        print(queue.pop(0))
    else:
        print(-1)
def size():
    print(len(queue))

def empty():
    return 1 if len(queue) == 0 else 0


def front():
    if empty() != 1:
        print(queue[0])
    else:
        print(-1)

def back():
    if empty() != 1:
        print(queue[len(queue) - 1])
    else:
        print(-1)


for _ in range(num):
    line = sys.stdin.readline().rstrip().split()

    if line[0] == "push":
        push(int(line[1]))
    elif line[0] == "pop":
        pop()
    elif line[0] == "size":
        size()
    elif line[0] == "empty":
        print(empty())
    elif line[0] == "front":
        front()
    else:
        back()