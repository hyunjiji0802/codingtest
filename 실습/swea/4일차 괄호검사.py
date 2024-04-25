T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    case = input()
    s = []
    a = True

    bracket_dic = {'(':')',
                '[':']',
                '{':'}'
                   }

    for i in case:
        if i in bracket_dic.keys():#여는 괄호를 찾으면
            s.append(i) #스택에 저장
        if i in bracket_dic.values(): #닫는 괄호를 찾으면
            if len(s)>0 and bracket_dic[s[-1]]==i: #스택이 비어있지 않고 여는 괄호와 종류가 동일하다면
                s.pop() #스택 pop
            else:
                a=False
                break
    if len(s)>0: #문장을 다 돌고 나서 스택이 비어있지 않다면
        answer=0
    elif a==False:#문장 중간에서 break했다면
        answer=0
    else:        #스택이 비어있다면
        answer=1
    print("#%d %d"%(test_case,answer))