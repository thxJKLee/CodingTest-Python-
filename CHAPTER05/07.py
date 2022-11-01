"""
BFS
Breadth First Search
너비 우선 탐색

1. 탐색 시작 노드를 큐에 삽입하고 방문처리 한다.
2. 큐에서 노드를 꺼내서 해당 노드의 인접노드중에서 
방문하지 않은 노드만 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번을 계속 방문해서 큐에 남는게 없도록 한다.

큐 는 정말 특별한 경우가 있지 않는한
계속 채워져 있는 형태라 Truly 형태

그래서 while문으로 queue의 상태를 꾸준히 체크하는 상태에서
v에 인접한 모든 노드. 즉 graph[v]의 원소를 모두 확인하여 큐에 넣어주는 작업과
그 노드를 방문했다고 표시만 해주면 된다.

이를 무한 반복하면 언젠가
큐가 비어져 있는 상태. 즉, Falsy 상태가 되므로 바로 탈출된다.
"""
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:  # queue가 비어있다면 Falsy이므로 탈출할 것이다.
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9

bfs(graph, 1, visited)
