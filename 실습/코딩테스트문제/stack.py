import sys

n = int(input())


class Stack:
    def __init__(self):
        self = []

    def push(self,num):
        print(self.append(num))

    def pop(self):
        if len(self) == 0:
            print(-1)
        else:
            print(self.pop())

    def size(self):
        print(len(self))

    def empty(self):
        if len(self) == 0:
            print(1)
        else:
            print(0)

    def top(self):
        if len(self) == 0:
            print(-1)
        else:
            print(self[len(self) - 1])


stack = Stack()
for _ in range(n):
    line = sys.stdin.readline().rstrip().split()

    if line[0] == "push":
        stack.push(int(line[1]))
    elif line[0] == "pop":
        stack.pop()
    elif line[0] == "size":
        stack.size()
    elif line[0] == "empty":
        stack.empty()
    else:
        stack.top()
