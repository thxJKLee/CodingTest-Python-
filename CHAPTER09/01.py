"""
최단 경로의 경우.
그리디 알고리즘과 다이나믹 프로그래밍을 사용한다고 생각할 수 있다.
1. 그리디 알고리즘의 경우, 당장 위치한 노드에서 최선의 간선만 골라갈 수도 있고
아니면 간선을 모두 오름차순으로 배열한 다음 최선의 간선을 골라가는 경우 [이거는 그리디 알고리즘이라고 하기에는 애매하겠지. 실시간으로 찾는건 아니니깐]
2. 점점 방문한 구역을 넓혀가는 것으로 생각하면 바텀업 방식의 다이나믹 프로그래밍이라고 생각할 수 있겠지.
""""""
다익스트라 최단 경로 알고리즘
1. 출발 노드를 설정
2. 최단 거리 테이블을 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 3~4 반복
"""
import sys
input = sys.stdin.readline
INF = int(1e9)

n, edge = map(int, input().split())
start = int(input())

graph = [[]for _ in range(n+1)]
# 1번 노드부터 n번 노드까지.
# 계산의 편리함을 위해 graph[0]은 빈 상태로하고 graph[1] 부터 graph[n] 까지 사용할 것임

visited = [False] * (n+1)
# visited[0] 은 아무것도 아니고
# 초기 상태에서는 1번 노드 부터 n번 노드까지 모두 방문하지 않은 상태

distance = [INF] * (n+1)
# distance[0] 은 아무것도 아니고
# 가능하면 값이 최소가 되도록 할 것이므로, INF로 초기값을 만들어 준다.
# 이 값은 노드를 지날때마다 갱신될 것이다.

for i in range(edge):
    # start 노드에서 end 노드까지 edge에 cost가 있으면 그것을 입력하는 연산이다.
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    # start -> end 이므로 graph[start]에 대입하는데, 이때 cost도 입력되어야 하므로 튜플 형태로 입력하였다.
    # 값의 변동도 없어야 하므로 리스트로 해도 되지만 튜플 형태로 했다.


def get_smallest_node():
    # 방문하지 않은 노드중에서 제일 작은 값을 반환한다.
    min = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min and not visited[i]:
            min = distance[i]
            index = i
    # 이곳에 도착하면 최종값은 다음과 같다.
    # distance 원소들이 바뀔 염려는 없고
    # 단순히 현재 distance 들 중에서 제일 작은 값을 찾아준다. 그리고 이를 반환한다.
    return index


def dijkstra(start):
    distance[start] = 0  # 최초 시작점은 거리가 0이다.
    visited[start] = True  # 최초 시작점을 방문했다고 표시한다.
    for j in graph[start]:  # start -> end 인 구역을 모두 확인한다.
        # 이때 j[0] 은 end 지점을 뜻하고
        # j[1] 은 cost를 뜻한다.
        distance[j[0]] = j[1]
        # 맨 처음에는 += 연산이 아니라 최초값을 만들어 준다.
    for i in range(n-1):  # 시작노드를 제외하고 나머지 부분에 대한 연산을 진행한다.
        now = get_smallest_node()  # 다음에 어느 노드를 갈지
        visited[now] = True  # 방문했다고 표시하고
        for j in graph[now]:
            # 일단 cost를 계산해준다. 조건에 따라 갱신할지 말지 결정할 것이다.
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:  # 연산한 값이 end 지점의 거리값보다 작으면
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
