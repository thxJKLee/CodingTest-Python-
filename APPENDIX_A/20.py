"""
파이썬에도 collections가 있음.

코딩테스트에서 활용되는 거는 주로
deque 와 Counter

1. deque
    => 인덱싱, 슬라이싱없이
    => 큐와 스택구조를 합친 형태.
    pop popleft
    append appendleft
    => 이유는 시간복잡도 때문인데. 이미 어느부분을 삭제하거나 추가하는것을 알고 있다면. 시간복잡도가 O(1) 
"""
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))
