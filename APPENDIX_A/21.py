"""
파이썬에도 collections가 있음.

코딩테스트에서 활용되는 거는 주로
deque 와 Counter

2. Counter
    => 등장횟수를 세는 경우.
    => 물론. find 함수나, re 모듈을 이용해서 찾을 수도 있지만.
    => 사용방식은, iterable을 인수로 넣어서 객체를 선언하면
    => key가 원소명, value가 갯수로 설정된 딕셔너리를 반환한다.(사실 정확히 딕셔너리는 아니다.)
"""
from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])
print(counter)
print(counter['blue'])
print(counter.keys())
print(counter.values())
print(counter.items())