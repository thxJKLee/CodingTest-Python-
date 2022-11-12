"""
bisect
간편한 이진탐색.
정렬된 배열에서 특정한 원소를 찾기위해.

1. bisect_left(a, x)
    => 정렬된 순서롤 유지하고 리스트 a에 x값을 왼쪽에 삽입할 위치 반환
2. bisect_right(b,x)
    => 정렬된 순서를 유지하고 리스트 a에 x값을 오른쪽에 삽입할 위치 반환
"""
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))  # 2번위치에 넣으면 되므로
print(bisect_right(a, x))  # 4번위치에 넣으면 되므로


print()

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index-left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))

print(count_by_range(a, -1, 3))
