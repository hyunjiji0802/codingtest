# from collections import deque
# import sys
# while True:
#     pair = True
#     arr = sys.stdin.readline().rstrip()
#     st= deque()
#     num = 0
#
#     if arr == '.': break
#
#     for i in arr:
#         if i == '(' or i == '[':
#             st.append(i)
#             num+=1
#         elif i == ')' and len(st) != 0:
#             num += 1
#             if st.pop() != '(':
#                 pair=False
#                 break
#         elif i == ']' and len(st) != 0 :
#             num += 1
#             if st.pop() != '[':
#                 pair=False
#                 break
#         elif (i == ']' and len(st) == 0) or (i == ')' and len(st) == 0) :
#             num += 1
#             pair = False
#             break
#
#     if (pair == True or num==0) and len(st)==0 :
#         print('yes')
#     else:
#         print('no')
#
#



import sys
from collections import deque

while True:
    l = deque(sys.stdin.readline().rstrip())
    if l[0] == ".":
        break

    stack = []
    answer = 'yes'

    while l:
        char = l.popleft()
        if char == '[' or char == '(':
            stack.append(char)
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                answer = 'no'
                break
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                answer = 'no'
                break

    if stack: answer = 'no'
    print(answer)
