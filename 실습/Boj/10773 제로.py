# from collections import deque
# import sys
# K=int(sys.stdin.readline().rstrip())
# d=deque()
# for _ in range(K):
#     num=int(sys.stdin.readline().rstrip())
#     if num == 0:
#         d.pop()
#     else:
#         d.append(num)
# sum=0
# for n in d:
#     sum+=n
# print(sum)

# import sys
# K = int(input())
#
# stack = []
# sum_stack = []
# for _ in range(K):
#     n = int(sys.stdin.readline().rstrip())
#     if n == 0:
#         sum_stack.append(stack.pop())
#     else:
#         stack.append(n)
# print(sum(stack))