##브루트 포스해결방식
##0-9 임의의 수를 가진 카드에서 6장을 뽑아
##6장의 카드가 모두 run(연속된 세 수) 이거나 triplete(동일한 세 수) 이면 Baby-gin

import itertools

babygin = list()

numbers = list(map(int,input("6자리수 입력: ").split()))

nPr = itertools.permutations(numbers,len(numbers))

for p in list(nPr):
    if (((p[0] + 1 == p[1]) and (p[1] + 1 == p[2])) or (p[0] == p[1] == p[2])) and (((p[3] + 1 == p[4]) and (p[4] + 1 == p[5])) or (p[3] == p[4] == p[5])):

        if p not in babygin:
            babygin.append(p)

print(babygin)




