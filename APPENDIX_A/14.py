"""
itertools
    => 반복되는 데이터를 처리할때 사용하는 라이브러리

1. permutations
리스트에서 몇 개를 선택하고 그것을 나열할지
"""
import numpy as np
from itertools import permutations  # 순열. nPr 같은거

print()

data = ['A', 'B', 'C']

result = list(permutations(data, 3)) # 

print(np.array(result))
