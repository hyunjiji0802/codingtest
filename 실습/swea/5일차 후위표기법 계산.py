T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
op = ['+','-','*','/']
for test_case in range(1, T + 1):
    post = input() #후위표기식 입력
    s = []
    exp = []
    for token in post:  # 후위표기 순회하면서 연산
        if token not in op: #피연산자이면
            s.append(token) #스택에 push
        else: #연산자이면
            if len(s)>1: #피연산자 두개 꺼내야함
                op1 = s.pop()
                op2 = s.pop()
                result = str(eval(op2+token+op1)) #피연산자의 순서 중요!! 먼저 꺼낸 애가 뒤로 & 연산 결과는 정수이므로 다시 str로 변환
                s.append(result) #연산 결과 다시push

                print(op2, token, op1, '=', result)
    print(int(float(s.pop()))) ## '-9.0' 은 정수형 문자열이 아니기 때문에, float으로 먼저 변환 후 int형으로 변환해야함!!