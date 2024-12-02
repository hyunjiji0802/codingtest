from sys import stdin
N = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().rstrip().split()))
answer = [0] * N
stack = []

for i in range(N):
    # 현재 탑의 높이가 스택의 탑보다 클 때 스택에서 제거
    while stack and stack[-1][0] < arr[i]:
        stack.pop()

    # 스택이 비어있지 않으면, 스택의 마지막 탑이 신호를 수신
    if stack:
        answer[i] = stack[-1][1] + 1  # 인덱스는 1부터 시작하므로 +1

    # 현재 탑 스택에 추가
    stack.append((arr[i], i))

print(*answer)

#시간초과 -> O(N^2)
# from sys import stdin
#
# N = int(stdin.readline().rstrip())
# arr = list(map(int, stdin.readline().rstrip().split()))
# answer = [0] * N
#
# cur_id = N - 1  # 현재 처리 중인 탑
# move_id = cur_id - 1  # 비교할 왼쪽 탑
#
# while cur_id > 0:
#     if move_id < 0:  # 비교할 왼쪽 탑이 없으면
#         cur_id -= 1  # 다음 탑으로 이동
#         move_id = cur_id - 1  # 새로운 왼쪽 탐색 시작
#     elif arr[move_id] >= arr[cur_id]:  # 높은 탑을 찾은 경우
#         answer[cur_id] = move_id + 1  # 신호를 수신한 탑 번호 기록
#         cur_id -= 1  # 다음 탑으로 이동
#         move_id = cur_id - 1  # 새로운 왼쪽 탐색 시작
#     else:  # 높은 탑을 못 찾으면
#         move_id -= 1  # 왼쪽으로 계속 이동
#
# # 결과 출력
# print(*answer)
