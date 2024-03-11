T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()

    new_a = list()
    for i in range(10):
        if i%2 == 0: #짝수면 큰 정수부터
            new_a.append(a[i//2])
        else :  #홀수면 작은 정수부터
            new_a.append(a[N-1-i//2])

    print("#%d"%(test_case), *(new_a))

