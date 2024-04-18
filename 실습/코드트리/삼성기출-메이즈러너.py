N, M, K = list(map(int, input().split()))
maze = [[10 for _ in range(N + 1)]]
for _ in range(N):
    l = list(map(int, input().split()))
    l.insert(0, 10)  ##기준이 1,1 이기 때문에 9 이상의 내구도인 경계 추가
    maze.append(l)

runners = [list(map(int, input().split())) for _ in range(M)]
exit = list(map(int, input().split()))
movement = 0
exit_x, exit_y = exit[1], exit[0]
# 0  1   2   3
# E  W   S   N
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for sec in range(K+1):  # K초동안 실행
    print("#K=",sec)

    for runner in runners:  # 각 참가자와 출구 거리 계산 후 현재 최단거리보다 가까워지도록 이동
        delta_x = exit[1] - runner[1]
        delta_y = exit[0] - runner[0]

        if delta_y > 0 and maze[runner[0] + dy[2]][runner[1] + dx[2]] == 0:  ##출구보다 위에 있고 벽이 없으면
            runner[1] += dx[2]
            runner[0] += dy[2]  # 아래로 한 칸 이동
            movement += 1
        elif delta_y < 0 and maze[runner[0] + dy[3]][runner[1] + dx[3]] == 0:  ##출구보다 아래에 있고 벽이 없으면
            runner[1] += dx[3]
            runner[0] += dy[3]  # 위로 한 칸 이동
            movement += 1
        elif delta_x < 0 and maze[runner[0] + dy[1]][runner[1] + dx[1]] == 0:  ##출구보다 오른 쪽에 있고 벽이 없으면
            runner[1] += dx[1]
            runner[0] += dy[1]  # 왼쪽으로 한 칸 이동
            movement += 1
        elif delta_x > 0 and maze[runner[0] + dy[0]][runner[1] + dx[0]] == 0:  ##출구보다 왼 쪽에 있고 벽이 없으면
            runner[1] += dx[0]
            runner[0] += dy[0]  # 오른 쪽으로 한 칸 이동
            movement += 1

        # print('이동 후 참가자 위치',runner)

    for runner in runners:
        if runner[1] == exit[1] and runner[0] == exit[0]:  # 탈출에 성공하면
            runners.remove(runner)  # runner에서 제거
            # print("남은 참가자 좌표",runners)

    # 이동 끝, 회전 시작
    # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 구하기
    left_top = []
    min_dis = 9999

    for runner in runners:
        # 좌상단, 우상단, 좌하단, 우하단

        rect = [[runner[0], runner[1]], [runner[0], exit[1]], [exit[0], runner[1]],[exit[0], exit[1]]]  # 출구와 참가자 1명을 포함한 직사각형 좌표
        rect.sort()
        w = abs(rect[3][1] - rect[0][1]) + 1  # 좌상단 - 우하단 가로길이
        h = abs(rect[3][0] - rect[0][0]) + 1  # 좌상단 - 우하단 세로길이

        print(rect)
        d = w if w > h else h
        if min_dis > d:  # 제일 작은 정사각형 길이 선정
            left_top = []
            min_dis = d
        elif min_dis == d:  # 같은 길이일 경우!!
            pass
        else:  # 더 크면 의미 없으므로 continue
            continue

        if w == h: #가로=세로 이면 정사각형 선정 완료
            left_top.append(rect[0])
            print(rect[0])
            continue
        # 가로 세로 길이 다르면 부족한 길이만큼 범위 키워주기
        else:
            dis = w - h if w > h else h - w  # 한변의 길이
            diff = rect[0][0] - 1 if w > h else rect[0][1] - 1  # (1,1)에서 좌상단 좌표까지 세로/가로 거리
            print(dis,diff)
            if w > h:  # 가로 길이가 더 긴 경우
                rect[0][0] -= diff  # 좌상단, 우상단 x좌표 -
                rect[1][0] -= diff
                rect[2][0] += dis - diff  # 좌하단, 우하단 x좌표 +
                rect[3][0] += dis - diff
            elif w < h:  # 세로 길이가 더 긴 경우
                rect[0][1] -= diff  # 좌상단, 좌하단 y좌표 -
                rect[2][1] -= diff
                rect[1][1] += dis - diff  # 우상단, 우하단 y좌표 +
                rect[3][1] += dis - diff
            left_top.append(rect[0])
            print(rect[0])

    print(left_top, min_dis)
    left_top.sort()  # r좌표 작고 c좌표 작은 것 우선
    print(left_top)
    min_rec = left_top[0]  # 좌상단 좌표 기준
    x, y = min_rec

    ##참가자 좌표 구해서 특이값 삽입 (-1씩 추가, 한 칸에 두 명 이상 있을 수 있음)
    for runner in runners:
        maze[runner[0]][runner[1]] -= 1

    maze[exit_y][exit_x] = -100

    for l in maze:
        print(l)

    new_maze = []
    for i in range(x, x + min_dis):  # 정사각형 크기만큼 슬라이싱
        temp_list = []
        for j in range(y, y + min_dis):
            temp_list.append(maze[i][j])
        new_maze.append(temp_list)

    print("작은 정사각형 결과")
    for r in new_maze:
        print(r)

    rotate_maze = [[0 for i in range(min_dis)] for j in range(min_dis)]  # 회전 결과를 담을 이차원 리스트

    # 시계방향으로 90도 회전
    for i in range(len(new_maze)):
        for j in range(len(new_maze[0])):
            if new_maze[i][j] > 0:  # 벽 내구도 감소
                rotate_maze[j][len(new_maze) - i - 1] = new_maze[i][j] - 1
            else:
                rotate_maze[j][len(new_maze) - i - 1] = new_maze[i][j]


    # 원래의 이차원 배열(maze)에 값 복사
    for i, ip in zip(range(x, x + min_dis), range(min_dis)):
        for j, jp in zip(range(y, y + min_dis), range(min_dis)):
            maze[i][j] = rotate_maze[ip][jp]

    print("회전 후 결과")
    for l in maze:
        print(l)

    runners = []  # 참가자 리스트 선언 및 참가자 탐색
    for i in range(N + 1):
        for j in range(N + 1):
            if maze[i][j] <= -100:  # 출구 좌표 반환
                maze[i][j] += 100
                exit_x = j
                exit_y = i
            elif maze[i][j] < 0:  # 두명 이상의 참가자가 있는 칸이면 좌표 반환
                while maze[i][j]<0:
                    maze[i][j] += 1
                    runners.append([i, j])
    print('현재 이동 횟수', movement)
    print('회전 후 참가자 좌표',runners)
    print('회전 후 출구 좌표', exit_y,exit_x)
    exit[0], exit[1] = exit_y, exit_x




print(movement, exit_x, exit_y)


