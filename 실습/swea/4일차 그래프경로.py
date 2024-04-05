T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    V_list = [[] for i in range(V+1)]
    stack = []
    answer = 0

    for i in range(E): #각 정점에서 연결된 관계를 리스트에 저장
        s,d = map(int, input().split())
        V_list[s].append(d)

    S, G = map(int, input().split())

    now_V = S
    stack.append(now_V)

    while True:
        if now_V == G: #경로 찾으면 break
            answer = 1
            break
        if len(V_list[now_V])==0: #인접 정점을 모두 방문했으면 스택 pop
            stack.pop()
            if len(stack)== 0: #스택이 비어있으면 순회끝
                answer = 0
                break
            now_V = stack[-1]
            # print(now_V,stack)
        else: #방문하지 않은 곳이 있으면
            now_V = V_list[now_V].pop() #해당 정점으로 이동
            stack.append(now_V) #정점을 스택에 push
            # print(now_V, stack)
    print("#%d %d"%(test_case,answer))