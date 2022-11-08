"""
신장트리.
그래프 형식을 트리구조로[정확한 답은 아님]

조금더 자세히 애기하면
하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프로 만드는 과정
"""
"""
크루스칼 알고리즘은 그리디 알고리즘
1. 간선 데이터를 비용에 따라 오름차 순으로 정렬
2. 간선을 하나씩 확인한다.
    i. 사이클이 발생한다면, 최소신장트리에 포함시키지 않는다.
    ii. 사이클이 발생하지 않는다면, 최소신장트리에 포함한다.
3. 모든 간선에 대하여 2번의 과정을 반복한다.

조금더 다르게 얘기하면

간선을 작은 순서대로 넣는다.
넣고나서 확인과정을 거친다.
[사이클이면 continue, 사이클이 아니면 넣기]
모든 간선에 대해 확인하기.
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 아예 부모가 루트노드가 되도록
    return parent[x]  # 목적은 부모를 출력하는 것이므로.


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())  # 노드의 개수와 간선의 개수(union연산횟수)
parent = [0]*(v+1)

edges = []  # 간선 테이블
result = 0  # 총 사용 비용

for i in range(1, v+1):
    parent[i] = i  # 1번노드 부터 v번 노드까지. 루트노드가 자기자신이라면 그 노드가 바로 최상단 부모


for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

"""
시간복잡도는
간선의 개수가 E이면

O(ElogE) 의 시간복잡도를 가진다.

정렬작업이 ElogE이고
나머지 작업은 해봤자 E 수준이다.
"""