"""
itertools
    => 반복되는 데이터를 처리할때 사용하는 라이브러리

2. combinations
리스트에서 몇 개를 선택할지.
"""
import numpy as np
from itertools import combinations  # 조합

print()

data = ['A', 'B', 'C']

result = list(combinations(data, 2)) # 

print(np.array(result))
