"""
itertools
    => 반복되는 데이터를 처리할때 사용하는 라이브러리

4. combinations_with_replacement
리스트에서 몇 개를 선택할지. 근데 중복해도 됨
"""
import numpy as np
from itertools import combinations_with_replacement  # 조합

print()

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2))

print(np.array(result))
