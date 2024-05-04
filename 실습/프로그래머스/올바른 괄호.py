def solution(s):
    stack = []
    answer = False
    for item in s:
        if item=='(': #여는 괄호면 스택에 push
            stack.append(item)
        else: #닫는 괄호면 스택 하나 pop해서 여는 괄호 꺼내기
            if len(stack) > 0 and stack.pop() == '(':
                pass
            else:
                return False
    if len(stack)>0: #스택이 비어있지 않으면 false
        answer = False
    else:
        answer = True
    return answer

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))