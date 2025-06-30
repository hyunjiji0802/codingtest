from collections import deque
N = int(input())
l = deque(list(map(int, input().split())))

order_stack = []
treat_stack = []


order_num = 1
while l:
    pop_num = l.popleft()

    if order_num == pop_num:
        treat_stack.append(pop_num)
        order_num+=1
    else:
        order_stack.append(pop_num)

    ##계속 이 줄에서 빠질 수 있다는 점
    while order_stack and order_num == order_stack[-1]:
        treat_stack.append(order_stack.pop())
        order_num+=1

    # print(treat_stack, order_stack)

sorted_stack = sorted(treat_stack + order_stack[::-1])

if sorted_stack == treat_stack + order_stack[::-1]:
    print('Nice')
else:
    print('Sad')