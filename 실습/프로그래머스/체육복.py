def solution(n, l, r):
    #여벌 체육복 가지고 온 학생 중 도난 당한 학생 제거
    new_r = list(set(r) - (set(r) & set(l)))
    new_l = list(set(l) - (set(r) & set(l)))
    if len(new_l)==0:
        return n
    else:
        answer = n - len(new_l)

    for l_num in new_l:
        if len(new_r)>0 and l_num-1 in new_r:
            r_num = new_r.index(l_num-1)
            print("%d 체육복 %d가 빌려줌"%(l_num,new_r[r_num]))
            new_r.pop(r_num)
            answer+=1
        elif len(new_r)>0 and l_num+1 in new_r:
            r_num = new_r.index(l_num+1)
            print("%d 체육복 %d가 빌려줌"%(l_num,new_r[r_num]))
            new_r.pop(r_num)
            answer+=1
    return answer

# print(solution(5,[2,4],[1,3,5]))
# print(solution(5,[3,4],[1,2,3]))
# print(solution(3,[3],[1]))
# print(solution(5,[2,5],[1,4]))
# print(solution(5,[1],[1,2]))
# print(solution(7,[2],[4]))
print(solution(5,[2,3],[3,4]))
