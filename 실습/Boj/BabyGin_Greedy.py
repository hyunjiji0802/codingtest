##탐욕알고리즘 해결방식
##0-9 임의의 수를 가진 카드에서 6장을 뽑아
##6장의 카드가 모두 run(연속된 세 수) 이거나 triplete(동일한 세 수) 이면 Baby-gin

COUNTS = [0 for _ in range(10)]

babygin = 0

numbers = list(map(int,input("6자리수 입력: ").split()))

for num in numbers:
    COUNTS[num] += 1

i=0
while i < len(COUNTS):

    if COUNTS[i]>=3:
        babygin+=1
        COUNTS[i]-=3
        # print("TRIPLETE!")
        continue

    if COUNTS[i] >=1 and COUNTS[i+1] >=1 and COUNTS[i+2] >=1: #RUN을 먼저 조사 할 경우 index error 발생
        babygin+=1
        COUNTS[i]-=1
        COUNTS[i+1] -= 1
        COUNTS[i+2] -= 1
        # print("RUN!")
        continue

    if babygin == 2:
        print("BABY-GIN", babygin)
        break

    i+=1
