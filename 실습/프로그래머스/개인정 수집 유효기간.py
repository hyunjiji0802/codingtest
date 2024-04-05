answer = 0

def solution(num):
    global answer
    if num == 1:
        return answer

    if answer >= 500:
        return -1
    else:
        answer+=1

    if num % 2 == 0:
        return solution(num // 2)  # 짝수일 경우 2로 나누어 재귀 실행

    else:
        return solution(num * 3 + 1)  # 홀수일 경우 3곱하고 1을 더해 재귀 실행

print(solution(626331))