n = int(input())
l = list(map(int, input().split()))
x = int(input())


cnt=  0


## 시간복잡도 ? 일단 정렬부터 하자 -> 투포인터라서 O(N) 임
## 정렬은 n log N 이라서 더 빠름

l.sort()
p1 = 0
p2 = n - 1

while p1 < p2:
    total = l[p1] + l[p2]
    if total == x:
        cnt+=1
        p1+=1
    elif total > x:
        p2-=1
    elif total < x:
        p1+=1

print(cnt)
