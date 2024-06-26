def solution(p):
    p.reverse()
    p = [[i, j] for i, j in
         zip(p, range(len(p)-1,-1,-1))]  # p[][0] 은 주식 가격,  p[][1]는 인덱스 정보

    s = []  # 스택에 차례로 담으며 가격 비교
    ans = [0 for _ in range(len(p))]

    # 초깃값
    s.append(p.pop())

    while p:  # p가 빌 때까지
        price = p.pop()  # 큐에서 가격 꺼내기
        if s[-1][0] <= price[0]:  # 가격이 떨어지지 않으면
            s.append(price)  # 스택에 추가
        else:  # 가격이 떨어졌으면
            while s and s[-1][0] > price[0]: #스택 내부 가격과 비교시작
                if s[-1][0] > price[0]:
                    st_price = s.pop() #스택 제일 위 원소 꺼내서
                    ans[st_price[1]] = price[1]-st_price[1] #해당하는 인덱스 정보에 시간 저장

            s.append(price)  # 스택에 추가
    #다 돌았으면 스택 비우기
    while s:  # s가 빌때까지
        print(s,ans)
        st_price = s.pop()
        ans[st_price[1]] = len(ans)-st_price[1]-1  # 나머지 정보 저장
    return ans
# print(solution([1,2,3,2,3]))

def solution2(p):
    t = 0
    answer = []
    for i in range(len(p)-1):
        if p[i] >= p[i+1]:
            t+=1
        else:
            pass

print(solution([1,2,3,2,3]))
# print(solution([1,2,3,1,2,0]))
