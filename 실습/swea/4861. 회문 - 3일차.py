'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.

[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

'''

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    l = [list(input()) for _ in range(N)]
    answer = False

    for i in range(N): #가로 회문 찾기
        for j in range(N):
            if j+M > N: continue
            if l[i][j:j+M] == list(reversed(l[i][j:j+M])):
                print("#%d %s"%(test_case, ''.join(l[i][j:j+M])))
                answer = True
                break

    if answer is True : continue
    l = list(zip(*l)) #전치 행렬 만들기

    for i in range(N): #세로 회문 찾기
        for j in range(N):
            if j+M > N: continue
            if list(l[i][j:j+M]) == list(reversed(l[i][j:j+M])):
                print("#%d %s"%(test_case, ''.join(l[i][j:j+M])))
                break
