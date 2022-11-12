"""
itertools
    => 반복되는 데이터를 처리할때 사용하는 라이브러리

3. product
리스트에서 몇 개를 선택할지 그리고 나열할지. 근데 중복해도 됨
"""
import numpy as np
from itertools import product  # 조합

print()

data = ['A', 'B', 'C']

result = list(product(data, repeat=2))

print(np.array(result))
