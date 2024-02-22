def solution(participant, completion):
    answer = ''
    dic = {}
    for p in participant:
        if dic.get(p) is None:
            dic[p] = 1
        else:
            dic[p] += 1

    for c in completion:
        dic[c] -= 1
        if dic[c] == 0:
            dic.pop(c)

    answer = list(dic.keys())
    return answer[0]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["marina", "nikola", "vinko", "filipa"]))