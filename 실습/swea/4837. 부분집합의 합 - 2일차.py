from itertools import combinations

T = int(input())
A = [i for i in range(1, 13)]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    # 부분집합
    c = combinations(A,N)
    sum_count = 0
    for set in c:
        if sum(list(set)) == K:
            sum_count+=1
    print("#%d %d"%(test_case, sum_count))