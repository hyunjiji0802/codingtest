T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    aj = list(map(int, input().split()))

    # sum_arr = [0 for _ in range(N-M)]
    sum_arr = list()
    for i in range(N-M+1):
        prefix_sum = 0
        for j in range(M):
            prefix_sum+=aj[i+j]
        # sum_arr[i] = prefix_sum
        sum_arr.append(prefix_sum)

    # print(sum_arr)

    print("#%d %d"%(test_case, max(sum_arr)-min(sum_arr)))