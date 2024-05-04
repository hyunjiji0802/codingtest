def solution(targets):
    answer_set = set()
    targets.sort(key=lambda x: (x[0],x[1]))
    tmp_answer = [0,0]

    for i in range(len(targets)):
        if targets[i][0] < tmp_answer[1]:  # 이미 겹치는 경우에는 continue
            continue
        elif targets[i][1] < tmp_answer[1]:
            continue
        else:
            tmp_answer = targets[i]
        j = i
        while targets[j][0]<targets[i][1]:
            if targets[j][0] < targets[i][1] and targets[j][0] >= targets[i][0]:  # 다른 미사일이 겹치는 경우. 오른쪽으로 겹칠 때
                if targets[j][0] > targets[i][0] and targets[j][1] <= targets[i][1]:  # 내부에 속해 있는 경우
                    tmp_answer[0] = targets[j][0]
                    tmp_answer[1] = targets[j][1]
                else:  # 오른쪽으로 겹치는 경우
                    tmp_answer[0] = targets[j][0]  # 뒤에있는 미사일의 시작부분으로 범위 좁히기
            j+=1
            if j==len(targets):
                break

        answer_set.add(tuple(tmp_answer))
    return len(answer_set)


# print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))
# print(solution([[1,3],[2,3],[2,3],[3,6]]))
# print(solution([[1,3],[1,3],[1,3]]))
# print(solution([[1,4],[2,6],[3,4],[3,9999]]))
# print(solution([[1,5],[2,7],[5,10],[7,8]]))
# print(solution([[3, 6], [2, 4], [5, 6], [1, 3]]))
# print(solution([[0,100000],[100,10000],[1000,9000],[5000,5001]]))
# print(solution([[1, 5], [3, 10], [3, 15], [5, 13],[10,15],[2,13]]))
print(solution([[1,100],[1,20],[1,4],[3,100],[3,10],[3,5]]))