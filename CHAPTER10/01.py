"""
서로소 집합.
몇몇 그래프 집합에서 중요하게 사용되는 편.


서로소 집합 자료구조
서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
union(합집합) find(찾기) 연산을 활용한다.

그래서 위에는 union-find 자료구조라고 불리기도 함.

보통 트리 자료구조로 집합으로 표현한다.

1. union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
    i. A와 B의 루트노드 A', B'를 각각 찾는다.
    ii. A'를 B'의 부모노드로 설정한다. (B'가 A'를 가리키도록 한다.)
2. 모든 union 연산을 처리할 때 까지 1번과정을 반복.
=> 보통 부모가 작은숫자가 되고, 자식이 큰 숫자가 되는 방식을 택한다[마치 최소힙 구조 처럼]

=> 완전히 나누어진 트리집합에서.
=> 두 집합의 루트를 부모/자식 관계로 만드는 것.

=> 보통 union 1,3 처럼 집합이 아니라 원소 자체를 작성한다.
=> 그리고 그 원소가 들어있는 서브트리가 있을텐데. 거기서 최상단 부모를 찾는다. 대충 a, b 라고 하자.
=> a > b 이면 a를 부모로, b를 a의 자식으로 만든다.
=> 그러면 두 서로소 집합이 합쳐지는게 완성된다.
=> 혹시나 두 원소(1,3)이 같은 부모를 가리킨다면, 아무일도 안일어나겠지.


다만 이러한 것도
연산의 속도를 늘리기 위해
노드 번호마다 부모가 누군지 바로 확인할 수 있는 테이블이 필요할 것이다.
"""


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


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

""" input
6 4
1 4
2 3
2 4
5 6
"""
"""output
각 원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블: 1 1 2 1 5 5 
"""
"""
만약 이러한 서로소 집합 구조에 대해
단순히 한줄로 구성된 집합으로 완성된다면 (1-2-3-4-5 .. 이런식)
그러면 find할 적에 O(V). 
이제 union이나 find도 여러번 한다면. 이게 M개라면 O(M).

합쳐서 O(VM) 만큼 되어서 비효율적이다.


하지만
경로압축을 통해 가능하면 부모 하나에 자식 여러개로 집중하는 방식이 좋긴하다.
이것은 02.py
"""
