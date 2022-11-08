"""
플루이드 워셜 알고리즘

모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우.


다익스트라 알고리즘하고 비교해서 생각하면.
단계마다 최단 거리를 가지는 노드를 하나씩 반복적으로 선택한다.
그리고 해당 노드를 거치는 경로를 모두 확인하고, 최단거리 테이블을 갱신하는것을 반복한다.

그래서 다익스트라를 기준으로 한다면 O(N^3) 수준의 복잡일 것이다.

그리고, 출발노드 1개만의 기준이 아닌 모든 경로를 출발노드인것처럼 모두 고려해야 하기 때문에
2차원 리스트로

간단한 원리는

A - B 비용이 13 이라고 하자.
만약
A - C - B 비용이 5 라면
A - B 비용을 5로 갱신한다.

그래서 알고리즘으로 생각하면
현재 확인하는 노드를 제외하고, N-1 개의 노드 중에서 서로 다른 노드 쌍을 찾는다.(A, B)
이후에
A -> 현재노드 -> B 로 가는 비용을 확인한 뒤 최단 거리를 갱신하면 된다. 

D_ab = min(D_ab , D_ak + D_kb)
"""
import numpy as np
INF = int(1e9)

n = int(input())  # 노드 갯수
m = int(input())  # 간선 갯수

graph = [[INF]*(n+1)
         for _ in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            # a와 b가 같으면 무조건 graph[a][b]가 제일 작을 것. 그러면 k가 무슨 값이든 상관 없음.
            # k가 a 나 b일경우. 자명하게 graph[a][b] + 0 형태라 제일 작을 것.
            # 그러므로 a!=b 라던가, a!=k and b!=k 인 경우를 굳이 조건문으로 작성할 필요가 없다.

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(f"{graph[a][b]:2d}", end=" ")
    print()
