from itertools import permutations, combinations
def solution(k, dungeons):
    p = permutations(dungeons, len(dungeons)) #순열 만들어서 완전탐색으로 풀기
    answer = 0
    for orders in p: #순열 리스트 = orders
        cnt = 0
        cur_k = k
        for min_st, use_st in orders: #각 순열에서 최소 스테미나, 사용 스테미나 뽑아서 계산
            if cur_k >=min_st:
                cur_k-=use_st
                cnt+=1
        answer = max(answer, cnt) #정답값 비교 후 업데이트
    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))