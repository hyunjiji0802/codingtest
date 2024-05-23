import sys
r,c = map(int,sys.stdin.readline().rstrip().split())
board = []
board.append([-1 for _ in range(c+1)])
for _ in range(r):
    l = [-1] #인덱스 1,1부터 시작이라 더미값 -1 넣어줌
    for i in sys.stdin.readline().rstrip():
        l.append(ord(i) - ord('A'))
    board.append(l)

for z in board:
    print(z)

    #상 하 좌 우
dc=[0,0,-1,1]
dr=[-1,1,0,0]

def dfs(cur_c, cur_r, count): #백트래킹 함수 선언(dfs 재귀)
    global max_len
    max_len = max(max_len, count)
    for i in range(4):
        nc, nr = cur_c + dc[i], cur_r + dr[i]
        if 0 < nc <= c and 0 < nr <= r and alpha_list[board[nr][nc]] is False:  # 지나온 알파벳 리스트에 없고(처음 밟는 알파벳) 범위 벗어나지 않으면
            alpha_list[board[nr][nc]] = True  # 다음 위치 알파벳 리스트에 저장, 방문 표시
            dfs(nc,nr,count+1) #다음 위치에서 dfs 수행
            alpha_list[board[nr][nc]] = False  # 방문 표시 해제

alpha_list = [False for _ in range(26)] #지나온 알파벳 리스트
alpha_list[board[1][1]] = True
max_len = 0

dfs(1,1,1)
print(max_len)
'''
# #두 번째 풀이
import sys
r,c = map(int,sys.stdin.readline().rstrip().split())
board = []
for _ in range(r):
    board.append(list(input()))

print(board)
    #상 하 좌 우
dc=[0,0,-1,1]
dr=[-1,1,0,0]

def dfs(cur_c, cur_r):
    max_len = 1
    stack = set([(cur_c,cur_r, board[cur_r][cur_c])]) #set으로 구현 (현재 컬럼, 현재 로우, 알파벳(A~Z))을 담은 셋
    while stack:
        cur_c,cur_r, alpha_visited = stack.pop()
        max_len = max(max_len, len(alpha_visited))

        for i in range(4):
            nc, nr = cur_c + dc[i], cur_r + dr[i]
            if 0 <= nc < c and 0 <= nr < r and board[nr][nc] not in alpha_visited:  # 알파벳 방문리스트에 없고(처음 밟는 알파벳) 범위 벗어나지 않으면
                stack.add((nc,nr,alpha_visited + board[nr][nc]))
        print(alpha_visited)

    return len(alpha_visited)

print(dfs(0,0))
'''