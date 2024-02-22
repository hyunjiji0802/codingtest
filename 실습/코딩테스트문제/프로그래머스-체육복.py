def solution(n, lost, reserve):
    answer = 0
    re_set = set(reserve)
    l_set = set(lost)
    sub = re_set & l_set
    l_list = list(l_set - sub)
    re_set = re_set - sub
    re_list = list(re_set)
    re_list.sort()

    for i in re_list:
        if i-1 in l_list:
            id = l_list.index(i-1)
            l_list.pop(id)
        elif i+1 in l_list:
            id = l_list.index(i+1)
            l_list.pop(id)
    l_num=len(l_list)
    # print(n, l_num)
    answer = n-l_num
    return answer


n=10
lost=[1,5,8,3,7]
reserve = [7,5,2,9,6]
# n = 5
# lost = [2,4]
# reserve = [1,3,5]
print(solution(n,lost,reserve))