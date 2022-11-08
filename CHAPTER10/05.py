"""
위상 정렬
방향 그래프의 모든 노드를 방향성에 거스리지 않도록 순서대로 나열하는 것.

위상수학은 사실 잘 모르긴 하지만
굳이 얘기하면

한줄로 압축한다고 생각하면 좋다.
그래서 값이 여러개 나올 수 있다.

알고리즘 자체는 아래와 같다.
1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음의 과정을 반복한다.
    i. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
    ii. 새롭게 진입 차수가 0이 된 노드를 큐에 넣는다.
    
다르게 얘기하면
어떤 노드 x는
출발하는 간선만 있다고 하자.
즉,
a->x 같은 간선이 없고
x->b 같 간선들만 있다고 하자.

그러면 그 노드 x를 큐에 넣고.
이제 그 노드 x를 다시 뺀다.
빼면서
x에서 출발하는 간선을 모두 제거한다.
[x->b 라던가 x->c 라던가]

그러면 분명 어떤 노드 y에 도착하는 간선이 제거되면서 0개가 될 수 있으므로
그 y를 다시 큐에 넣는다.

이것을 큐가 확실히 빌 때까지 적용한다.
하지만. 큐가 중간에 빌 가능성이 있는데.
이는 사이클이 있다고 생각하면 된다. a - b - c - a 라면 모두 진입차선이 1개 이상이다.


그러면 이걸 알고리즘에서 쓴다면.
진입차수 테이블을 따로 설정하면 편할 것이다.
"""
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

# a->b 인 간선들을 전부 입력한다.
# 그러면 그래프에는 graph[a] 에 값이 추가 될 것이고
# 진입간선의 갯수는 b에 추가될 것이다.
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()

"""
위상정렬을 단순히 생각해보면
1.차례대로 모든 노드를 확인한다.
2. 해당 노드에서 출발하는 간선을 차례로 제거해야한다.(다 합치면 모든 간선의 갯수 수준일 것이다.)
그래서 O(V+E)
"""