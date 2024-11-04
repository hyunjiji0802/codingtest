import heapq as h
def solution(scoville, K):
    heap = []
    for value in scoville:
        h.heappush(heap,value)

    mixed_num = 0

    if heap[0] >= K: #애초에 안섞어도 되면그냥 0 반환
        return mixed_num

    while heap and heap[0] < K: #모든 음식의 스코빌 지수가 K 이상이 될 때 까지
        first = h.heappop(heap)
        if len(heap)>=1: #섞을 수 있는 경우
            second = h.heappop(heap)

            mixed = first + (second * 2)
            mixed_num+=1

            h.heappush(heap,mixed)
        else: #섞을 수 없는 경우
            h.heappush(heap,first)
            break

    if heap[0] >= K:
        return mixed_num
    else: #모든 음식의 스코빌 지수를 K이상으로 못만들면
        return -1

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2, 3, 9, 10, 12], -100))
print(solution([1, 2, 3, 9, 10, 12], 1000))