def solution(want, number, discount):
    answer = 0
    want_dic = {}

    for i in range(len(want)):
        want_dic[want[i]] = number[i]
    # 투포인터
    # print(want_dic)
    i=0
    while i <= len(discount)-10:
        # print(i,i+10, discount[i:i+10], len(discount[i:i+10]))
        #기준일부터 열흘동안의 리스트 추출
        discount_dic = {}
        for item in discount[i:i+10] :
            discount_dic[item] = discount[i:i+10].count(item)

        # print(i,discount_dic)
        flag = False
        #want_dic과 discount_dic 키 값 비교
        if discount_dic == want_dic: #딕셔너리가 같으면
            answer += 1
        i+=1
    return answer


print('answer:',
    solution(
        ["banana", "apple", "rice", "pork", "pot"],
        [3, 2, 2, 2, 1],
        ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana",]
        ))

print('answer:',
    solution(
    ["apple"],
    [10],
    ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
    )
)

print('answer:',
    solution(
    ["apple","banana", "copy"],
    [6,3,1],
    ["banana", "banana", "banana", "banana", "banana", "apple","apple", "apple", "apple", "apple", "banana", "apple", "copy"]
    )
)