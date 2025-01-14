def solution(n, m, section):
    arr = [0] * n
    for i in section:
        arr[i-1] = 1
    answer = 0

    # print(arr)
    for i in range(n-m+1):
        if arr[i] == 1:
            for j in range(m):
                arr[i+j] = 0
            answer+=1

    if 1 in arr[-m:]:
        answer+=1

    return answer

print(solution(8,4,[2,3,6]))