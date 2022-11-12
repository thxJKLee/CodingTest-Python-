"""
다시온 순열과 조합인데.

그 값은 마치
리스트의 리스트 방식으로 값을 얻는다.
[정확히는 리스트는 아니라 리스트로 변환하는 과정이 있으면 좋다.]

그러므로 for문으로 가져오면
말그대로 각각의 경우를 확인할 수 있다.
"""
import itertools

data = [1,2]

for x in itertools.permutations(data,2):
    print(list(x))
    
print()
    
data = [1,2,3]

for x in itertools.combinations(data,2):
    print(list(x))