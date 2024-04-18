T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s = list(input())
    i=0
    while True:
        if i>=len(s):
            print("#%d %d"%(test_case,len(s)))
            break
        if i+1<len(s) and s[i]==s[i+1]:
            if i==0:
                s = s[i+2:]
                i = 0
            elif i==len(s)-2:
                s = s[:i]
                i -=2
            elif i>0 and i<len(s)-2:
                s = s[:i]+s[i+2:] #반복 문자 제거 후 이어 붙이기
                i -=1 #탐색 인덱스 조정
        else:
            i+=1
        if i<0: i=0

