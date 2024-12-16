import random

# 참여자와 문제 리스트
participants = ["현지", "경연", "서진", "서연"]
problems = ["1","2","3","4","5"]

# 문제를 섞기
random.shuffle(problems)

# 사다리 타기 결과 생성
results = {}
for i, participant in enumerate(participants):
    if problems:
        results[participant] = problems.pop(0)

# 남은 문제가 있으면 랜덤하게 한 명에게 추가 배정
if problems:
    extra_problem = problems.pop(0)
    extra_person = random.choice(participants)
    results[extra_person] += f", {extra_problem}"

print(results)