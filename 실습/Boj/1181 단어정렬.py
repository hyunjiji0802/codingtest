import sys
N=int(input())
arr=[]
for _ in range(N):
    word=sys.stdin.readline().rstrip()
    arr.append(tuple([word, len(word)]))

#중복 제거 set()메소드
arr=list(set(arr))

arr.sort(key=lambda x:(x[1],x[0]))
for i in arr:
    print(i[0])