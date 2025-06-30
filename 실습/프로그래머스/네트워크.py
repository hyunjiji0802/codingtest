# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return


def solution(n, computers):
    answer = 0
    # 일단 모든 노드 방문 리스트
    visited = [False for _ in range(n)]

    def dfs(i):
        # 방문 체크
        visited[i] = True

        # 이웃 탐색하기
        for j in range(n):
            # 나 말고, 다른 컴퓨터 이어져있고, 방문한 적 없으면
            if i != j and computers[i][j] == 1 and visited[j] == False:
                dfs(j)

    for i in range(n):
        if visited[i] == False:
            # 방문한 적 없으면
            dfs(i)
            # 네트워크 수 + 1
            answer += 1

    return answer
