"""
서로소 집합은 여러곳에 활용가능함.
1. 무방향 그래프에서의 사이클 여부 판별
[방향 그래프에서는 DFS를 이용하여 판별 가능하다. => 대충 원리로 판단하면 노드수이상 반복해도 계속 다음 값이 있으면 사이클이 되는걸로 판별되려나]

union 연산은 그래프에서 간선으로 생각할 수도 있다.
그래서 간선을 하나씩 살펴보면서 두 노드가 포함되어 있는 집합을 합치는 과정을 반복하는 것만으로 사이클을 판별할 수 있을듯
1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
    i. 루트노드가 서로 다르다면 두 노드에 대해 union
    ii. 루트노드가 서로 같다면 사이클(Cycle)이 발생한 것
2. 그래프에 포함되어 있는 모든 간선에 대해 1번 과정을 반복.

예를들어
처음에는 당연히 사이클인지 알 수 없다.

하지만 충분한 union을 진행한다음.
확인안한 간선을 확인해보자.
만약 루트노드가 동일하다면 서로 연결되어 있다는것이다. 즉 사이클
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
for i in range(1, v+1):
    parent[i] = i  # 1번노드 부터 v번 노드까지. 루트노드가 자기자신이라면 그 노드가 바로 최상단 부모

cycle = False


for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생함")
