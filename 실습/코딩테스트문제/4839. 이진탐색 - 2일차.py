global Count_Num
def binarySearch(l, r, k, count):
    count+=1
    if l > r : #검색 실패
        return
    else:
        m = int((l+r)/2)
        if m == k: #탐색 성공
            global Count_Num
            Count_Num = count
            return
        elif m > k :
            binarySearch(l, m, k, count)
        else:
            binarySearch(m, r, k, count)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, Pa, Pb = list(map(int, input().split()))
    #이진 탐색 시작
    binarySearch(1,P,Pa,0)
    A_count = Count_Num
    binarySearch(1,P,Pb,0)
    B_count = Count_Num

    if A_count == B_count :
        result = 0
    else:
        result = "A" if A_count < B_count else "B"

    print("#%d"%(test_case),result)
