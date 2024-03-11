T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    m_arr = [0 for _ in range(N+1)]

    count = 0
    for i in range(len(m_arr)):
        if i in arr:
            m_arr[i] = K

    i = 0
    while i<N:
        temp_arr = m_arr[i + 1:i + K + 1]
        temp_arr.reverse()
        if K in temp_arr: #갈 수 있는 최대 정거장까지 충전기 위치 구하기
            id_num = i+K - (temp_arr.index(K))  #갈 수 있는 최대 정거장 거리에서 제일 뒤에 있는 충전기 위치 확인
            i = id_num
            count += 1
            if i+K>=N:
                break
        else:
            count = 0
            break   #만약 갈수 있는 최대 정거장 내에서 충전기가 없으면 정류장이 잘못 설치됨
    print("#%d %d"%(test_case,count))
