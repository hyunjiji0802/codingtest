T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) // 10
    arr = [0 for i in range(31)]
    arr[1] = 1
    arr[2] = 3

    for i in range(N + 1):
        if i > 2:
            arr[i] = arr[i - 1] + 2 * arr[i - 2]
    print("#%d %d"%(test_case, arr[N]))