grid = []
goal = tuple()
for idx in range(10):
    tmp = list(map(int, input().split()))
    grid.append(tmp)

    if 2 in tmp:
        goal = (idx, tmp.index(2))

cur_r, cur_c = 1,1
while True:

    # 현재 위치 표시
    grid[cur_r][cur_c] = 9

    # 맨 아래 가장 오른쪽에 도착한 경우           # 더 이상 움직일 수 없는 경우 -> 오른쪽, 아래 모두 벽이라면
    if ((cur_r == 8) and (cur_c == 8)) or \
    ((grid[cur_r][cur_c + 1] == 1 and grid[cur_r + 1][cur_c] == 1)) or \
    (cur_r == goal[0] and cur_c == goal[1]): # 먹이를 찾은 경우
        break

    #오른쪽으로 움직일 수 있으면
    if grid[cur_r][cur_c + 1] != 1:
        #오른쪽으로 이동
        cur_c += 1
    #오른쪽에 벽이 있으면
    elif grid[cur_r][cur_c + 1] == 1:
        #아래로 이동
        cur_r +=1
    else:
        break

for g in grid:
    print(*g)