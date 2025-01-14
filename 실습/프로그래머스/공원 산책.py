def solution(park, routes):
    arr = []
    cur_r, cur_c= 0,0

    for r in range(len(park)):
        tmp = []
        for c in range(len(park[0])):
            if park[r][c] == 'S':
                cur_r, cur_c= r,c
            tmp.append(park[r][c])
        arr.append(tmp)

    for route in routes:
        d, m = route.split()
        m = int(m)
        if d == "E" and 0<=cur_c + m < len(arr[0]) and "X" not in arr[cur_r][cur_c:cur_c+m+1]:
            cur_c = cur_c + m
        if d == "W" and 0 <= cur_c - m < len(arr[0]) and "X" not in arr[cur_r][cur_c - m:cur_c+1]:
            cur_c = cur_c - m
        if d == "N" and 0<= cur_r - m < len(arr) and "X" not in [a[cur_c] for a in arr[cur_r - m:cur_r+1]]:
            cur_r = cur_r - m
        if d == "S" and 0<= cur_r + m < len(arr) and "X" not in [a[cur_c] for a in arr[cur_r:cur_r + m+1]]:
            cur_r = cur_r + m
    return [cur_r, cur_c]

print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))