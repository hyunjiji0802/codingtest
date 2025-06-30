from collections import deque
T = int(input())
for _ in range(T):
    stack = []
    answer = 'YES'
    s = deque(input())

    while s:
        item = s.popleft()
        if item == '(':
            stack.append(item)
        elif item == ')': #닫는괄호만나면 여는괄호 만날때까지 stack pop
            if not stack:
                answer = 'NO'
                break

            while stack:
                if stack[-1] == '(':
                    stack.pop()
                    break
    print('NO' if stack else answer)


