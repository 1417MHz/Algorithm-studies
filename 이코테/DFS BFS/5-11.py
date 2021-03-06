# BFS
# p.154

# 사람이 n*m크기의 미로에 갇혀있다. 미로에는 여러 괴물이 있어 이를 피해 탈출해야 한다.
# 사람의 위치는 (1, 1)이고 미로의 출구는 (n, m)에 있다. 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시한다.
# 이때 사람이 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. (시작 칸과 마지막 칸을 모두 포함해서 계산한다)

from collections import deque

n, m = map(int, input().split())

# 미로 정보 입력받기(2차원 리스트)
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# 이동할 네 방향 정의하기 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 메소드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어날 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 위치한 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
