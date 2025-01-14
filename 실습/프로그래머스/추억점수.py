def solution(name, yearning, photo):
    answer = []
    dic = {n:score for n, score in zip(name, yearning)}

    for p in photo:
        sum = 0
        for people in p:
            sum += dic.get(people, 0)
        answer.append(sum)
    return answer

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]] ))