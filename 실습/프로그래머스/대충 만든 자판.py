def solution(keymap, targets):
    answer = []
    d = {}
    for key in keymap:
        for i, s in enumerate(key):
            if s in d:
                d[s] = min(d[s], i+1)
            else:
                d[s] = i+1
    for target in targets:
        count = 0
        for s in target:
            if s in d:
                count+=d[s]
            else:
                count = -1
                break
        answer.append(count)
    return answer

print(solution(["AGZ", "BSSS"],	["ASA","BGZ"] ))
print(solution(["ABACD", "BCEFD"],["ABCD","AABB"] ))
print(solution(["AA"],["B"] ))