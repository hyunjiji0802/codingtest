T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
op = {'+': 1,
      '-': 1,
      '*': 2,
      '/': 2,
      '(': 0
      }
for test_case in range(1, T + 1):
    exp = input() #계산식 입력

    s = []
    answer = []
    for token in exp: #계산식 순회하면서 후위표기 실행
        if token in op.keys(): #연산자인경우
            if len(s)==0: #스택이 비어있으면 push
                s.append(token)

            elif op[token]>op[s[-1]] or token =='(': #스택의 top과 비교했을 때 토큰의 우선순위가 높은 경우 & 스택 밖의 여는 괄호는 우선순위가 가장 높으므로 바로 push
                s.append(token) #스택에 push

            else: #우선순위가 낮거나 같은 경우
                while len(s)>0: #스택이 비어있지 않은 경우
                    if op[token] > op[s[-1]]:#토큰의 우선순위가 연산자의 우선순위보다 높을 때 까지 pop
                        s.append(token)  # 해당 연산자 push
                        break
                    else:
                        oper = s.pop()
                        if oper !='(' and oper !=')': #괄호는 출력하지않음
                            answer.append(oper)

        elif token == ')' :  # 토큰이 닫는 괄호일 경우
            while len(s) > 0:
                oper = s.pop()
                if oper == '(':  # 여는 괄호 나올 때 까지 stack pop
                    break
                elif oper == ')':
                    pass  # 닫는 괄호를 만나면 출력X pass
                else:  # 연산자 출력
                    answer.append(oper)

        else: #토큰이 피연산자(숫자)인 경우
            answer.append(token)

    #계산식 다 돌면 스택에 남은 모든 연산자 pop&출력
    while len(s)>0:
        oper = s.pop()
        if oper !='(' and oper !=')':
            answer.append(oper)
    print(*answer)