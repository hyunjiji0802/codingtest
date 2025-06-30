def solution(n, times):

    max_t = max(times) * n + 1  ## 느림보가 혼자 다 할때
    min_t = 0               ## 최소

    t = (max_t + min_t) // 2

    answer = 1000000001

    while min_t <= max_t: ##범위 내 탐색
        #t분간 지나간 사람 수 세기
        tmp = [t // minutes for minutes in times]
        # print(tmp, t, answer, max_t, min_t)
        cnt = sum(tmp)

        # print(min_t, max_t, cnt)
        #t분동안 다 못지나가면 시간 +
        if cnt < n:
            min_t = t + 1
        #t분동안 지나간 사람이 n보다 많으면
        elif cnt >= n:

            max_t = t - 1
            answer = t

        t = (max_t + min_t) // 2

    return answer

n = 6 ; times = [7,10]


print(solution(n, times))