"""
DFS
Depth-First Search
깊이 우선 탐색

node = vertex
edge

여기서는 인접 리스트 방식
"""
graph = [[] for _ in range(3)]

graph[0].append((1, 7))  # (노드, 거리)
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)

"""
인접 행렬 방식은 메모리 낭비가 심하지만 속도가 빠르다.
단순히 1과 7의 연결을 확인하고 싶으면 graph[1][7]로 확인하면 된다.

인접 리스트 방식은 메모리를 최소한 사용하지만 속도가 느리다.
1과 7의 연결을 확인하고 싶다면 
graph[1] 에 있는 원소를 하나씩 확인하거나
graph[7] 에 있는 원소를 하나씩 확인하여 노드값이 일치하는 부분을 찾으면 된다.
"""