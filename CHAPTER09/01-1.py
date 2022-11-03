"""
단순히 이론상으로 간단하게 하는 다익스트라는 시간복잡도가 큰 편이다.
O(V^2).. 이떄 V는 노드의 갯수이다.

1. 최단거리가 짧은 노드를 찾을때 V번
2. 현재 노드와 연결된 노드를 매번 확인 < V 번
""""""
import sys
개선한 경우의 아이디어를 알아보기 전에

힙 을 알아보자.
=> 구현자체를 할 생각은 없다.

1. 우선순위 큐의 한 종류
=> 우선순위가 가장 높은 데이터를 가장 먼저 삭제

PriorityQueue 또는
heapq => 이거 권장

최소힙 => 값이 낮은 데이터가 먼저 삭제되도록 => 기본값
최대힙 => 값이 큰 데이터가 먼저 삭제되도록 ==> 여기서 테크닉은, 모든데이터에 -1을 곱하여 저장한 뒤, 꺼낼 때 -1을 다시 곱하면 그게 최대힙이 될 수 있다.


우선순위 큐에서도
1. 리스트로 구현하는 경우
=> 삽입 O(1) / 삭제 O(N)
=> 넣을때 정렬하지 않지만, 매번 삭제할때마다 최소값을 찾아야 한다.

2. 힙으로 구현하는 경우
=> 삽입 O(logN) / 삭제 O(logN)
=> 넣을때도 정렬하고, 삭제할때도 매번 정렬한다.
=> 하지만, 이진 트리 형태이기 때문에 언제나 logN(깊이) 수준정도 소모한다.

위의 연산을 모든 데이터를 넣은 뒤, 모든 데이터를 뺀다면
2NlogN
=> O(NlogN) 이 된다.
""""""
아무튼 결론만 말하면
가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가적으로 이용한다는 점이다.
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, edge = map(int, input().split())
start = int(input())

graph = [[]for _ in range(n+1)]

distance = [INF] * (n+1)

for i in range(edge):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))


# def get_smallest_node():
#     min = INF
#     index = 0
#     for i in range(1, n+1):
#         if distance[i] < min and not visited[i]:
#             min = distance[i]
#             index = i
#     return index


def dijkstra(start):
    q = []  # 기본값으로 빈 큐
    heapq.heappush(q, (0, start))  # q에 (거리, 시작노드)를 넣는다.
    distance[start] = 0  # 거리 배열에도 0을 대입한다.
    while q:  # q는 언젠간 다 사라진다. 그래도 못간 간선이 있다면, 홀로 떨어진 섬이라고 해석할 수 있다.
        dist, now = heapq.heappop(q)  # q에서 빼오는 값은 제일 작은 거리값과 노드위치
        # 만약 현재 거리값이 빼온 최소거리값보다 작으면, 굳이 갱신할 필요 없으므로 다음 노드를 살펴본다.
        if distance[now] < dist:
            continue
        # 역대 최저거리값은 여기에 도착할 것이다
        for i in graph[now]:  # 현재 노드 위치 -> end 부분의 값들을 모두 살펴본다.
            cost = dist + i[1]
            if cost < distance[i[0]]:  # 만약 현재 값보다 더 작은 거리 값이 발견되면 [여러번 발견될 수도 있음]
                distance[i[0]] = cost  # 갱신하고
                heapq.heappush(q, (cost, i[0]))  # 큐에다가도 넣는다. (거리값, 노드값)


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
