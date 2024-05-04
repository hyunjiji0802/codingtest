def solution(s, k):
    start_i, i = 0, 0
    s_sum = 0
    answer = [1, 1000001]
    while i < len(s):
        # start_i 부터 i까지 부분수열의 합 구하기
        s_sum += s[i]
        print(s_sum,start_i,i,answer)
        if s_sum == k:# 부분 수열의 합이 k 일 경우
            if i - start_i < answer[1] - answer[0]:  # 수열의 길이 비교, 더 짧으면
                answer = [start_i, i]
                if start_i == i:  # 수열의길이 1이면 정답이므로 바로 리턴
                    break
            s_sum -= s[start_i]
            s_sum -= s[i]
            start_i +=1

        elif s_sum > k:
            if start_i == i:
                break
            else:
                s_sum -= s[start_i]
                s_sum -= s[i]
                start_i += 1
        else:
            i += 1
    return answer

print(solution([1,1,1,1,1,1,5], k=5))