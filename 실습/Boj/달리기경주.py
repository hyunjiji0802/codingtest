def solution(players, callings):
    d = dict()
    for i, p in enumerate(players):
        d[p] = i

    for player in callings:
        a = d[player]
        for k, v in d.items():
            if v == a-1:
                d[player] -= 1
                d[k] += 1
    d = sorted(d.items(), key = lambda x:x[1])
    return [c[0] for c in d]

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))