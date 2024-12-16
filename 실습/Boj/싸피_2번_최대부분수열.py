T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    sum_list = [sum(A[i:i + 2]) for i in range(len(A) - 1)]
    print(sum_list)
    sum_list.sort()

    print("#%d %d"%(tc,sum(sum_list[-K:])))

# 입력 예
# 3
# 6 2
# 2 4 3 -4 6 1
# 4 1
# 3 4 5 1
# 4 2
# -2 -3 -4 -1
#
# 출력 예
# #1 14
# #2 9
# 3 -10


