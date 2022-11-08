def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # 아예 부모가 루트노드가 되도록
    return parent[x] # 목적은 부모를 출력하는 것이므로.


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

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
"""
노드의 개수가 V개
최대 V-1개의 union 연산
M개의 find 연산.

==>
O(V+M(1+log_(2-M/V)[V]))
대충 V가 1,000
union연산 + find 연산의 갯수가 1,000,000
그러면 약 10,000,000 번의 연산이다.


더 줄일수 있는 방법이 있긴 한데
코딩테스트에서는 이정도만 기억해두면된다.[즉, 경로압축부분]
"""