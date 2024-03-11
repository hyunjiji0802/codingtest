arr = [3,6,7,1,5,4]

n = len(arr)

"부분집합 전부 출력"

for i in range(1<<n): #부분집합의 개수만큼 반복
    for j in range(n): #원소의 포함 여부 판단 가능
        if i&(1<<j): #i 의 j 번째 비트가 1이면 j 번 째 원소 출력
            print(arr[j], end=', ')
    print() 