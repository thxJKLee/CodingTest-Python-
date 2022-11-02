"""
퀵정렬

기본적으로 재귀함수 형태로 사용한다.
array의 길이가 N 이라고 하자.

1. array[0] 을 pivot이라고 하자. 기준 값이 될 것이다.
2. i는 1, j는 N-1로 정한다.
3. array[i] < pivot 일 경우 i++ [반복]
4. pivot < array[j] 일 경우 j-- [반복]
5. 3번도 따로 반복하고, 4번도 따로 반복한다.
그러면 array[i] > pivot > array[j] 가 성립되는 구역까지 도착할텐데. array[i] 와 array[j]를 스왚
6. 5번을 진행하다보면 i>=j인 구간이 발생한다. array[i]와 array[j] 중 작은값과 array[0]를 스왚
그러면 pivot의 위치라 변경됐을 텐데. 왼쪽은 자명하게 pivot보다 작은값, 오른쪽은 pivot보다 큰 값이 될 것이다.
7. pivot을 기준으로 왼쪽 배열과 오른쪽 배열이 있을텐데. 그 작은 배열에 대해서 1~6번 작업을 다시 실행한다.
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))

"""
위는 파이썬의 기능을 적절히 활용한 방식이라 계산량은 좀 많을수 있다.
"""
