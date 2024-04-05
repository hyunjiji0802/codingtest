def solution(friends, gifts):
    answer = 0 #가장 많이 받은 선물
    map_dic = {} #사람 이름 - id로 mapping
    new_gifts=[] #maxrix 생성하기 위해 사람 이름 문자열을 숫자 id로 replace

    get_value = []  #gift_value 계산하기 위해 각 사람마다 받은 선물 수 계산하는 리스트
    give_value = [] #gift_value 계산하기 위해 각 사람마다 보낸 선물 수 계산하는 리스트
    gift_value =[]  #선물 지수 리스트

    next_month_gift=[0 for _ in range(len(friends))]    #다음달에 받을 선물 수 리스트

    matrix = [[0 for _ in range(len(friends))] for i in range(len(friends))]    #[선물 보낸 사람, 선물 받은사람] 2차원 리스트

    i = 0

    #사람 이름 str를 int id로 mappin하기 위해 map_dic에 저장
    for name in friends:
        map_dic[name] = i
        i += 1

    #gifts의 "A B" 형식 str 원소를 [0,1] 리스트 원소와 같이 변경하여 new_gifts에 저장
    for gift in gifts:
        give,get = gift.split()
        A = map_dic[give]
        B = map_dic[get]

        new_gifts.append([A,B])

    #matrix에 선물 주고받은 인덱스에 해당하는 원소를 1만큼 추가
    for id in new_gifts:
        matrix[id[0]][id[1]]+=1

    #선물 지수 구하기
    for l in list(zip(*matrix)):
        get_value.append(sum(l))
    for l in matrix:
        give_value.append(sum(l))

    for give,get in zip(give_value,get_value):
        gift_value.append(give-get)

    #maxtrix 순회하면서 조건 비교
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i==j: continue #같은 사람끼리는 비교 X
            if matrix[i][j]>matrix[j][i] : #선물을 주고받은 기록이 있고 i가 선물을 더 많이 줬다면
                next_month_gift[i]+=1

            elif matrix[i][j] - matrix[j][i] == 0: #선물 주고 받은 기록이 없거나 주고받은 수가 같다면
                if gift_value[i] > gift_value[j]:
                    next_month_gift[i]+=1

    answer = max(next_month_gift)
    return answer

print(solution(["a", "b", "c"],["a b", "b a", "c a", "a c", "a c", "c a"]))