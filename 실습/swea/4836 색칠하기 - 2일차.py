T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    rows = 10
    cols = 10
    id_list = [[0 for _ in range(cols)] for _ in range(rows)]
    N = int(input())

    for n in range(N):
        r1, c1, r2, c2, color = list(map(int,input().split()))
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                id_list[r][c]+=color

    purple = 0
    for i in range(rows):
        purple+=id_list[i].count(3)

    print("#%d %d"%(test_case, purple))