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


def quick_sort(arr, start, end):  # 원본 배열, start인덱스 end인덱스
    if start >= end:  # start와 end가 같다던가, start가 오히려 end를 역전하는 경우
        return  # 아무것도 실행하지 않는다.
    pivot = start  # pivot을 제일 우측에 있는 값
    left = start+1  # pivot 다음 위치를 left
    right = end  # 맨 마지막 위치는 right
    while left <= right:  # left > right인 경우 탈출하게 될 것임
        # left가 범위내에 있어야하며, pivot 왼쪽에는 확실히 작은값만 있어야 하니깐.무시하면 되므로
        while left <= end and arr[left] < arr[pivot]:
            left += 1
        # 역시 right가 범위내에 있어야 하는데 start보다는 커야할 것이고, pivot 오른쪽에는 확실히 큰 값만 있어야 하니깐, 무시하면 그만
        while start < right and arr[pivot] <= arr[right]:
            right -= 1
        # 결론적으로 이쪽에 도착하는 경우는 arr[left] >= pivot > arr[right] 인 경우이므로 arr[right]가 무조건 작은 값일 것이다.
        if left > right:  # 만약 탈출했을 경우. 그런데 left > right인 경우에는 이미 비교할 필요 없이 역전된 것이므로
            # 작은값인 arr[right] 와 arr[pivot]을 바꿔준다.
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:  # 탈출했는데 아직 left와 right가 역전되지 않았으면
            # arr[left]<pivot<=arr[right] 형태가 되도록 스왚해준다.
            arr[left], arr[right] = arr[right], arr[left]
    # 그러면 우리가 가지고 있던 pivot부분이 right 자리로 이동된 셈이다.
    # 그러면 right부분을 제외한 나머지 두 부분에 대해 quick_sort를 진행해주면 된다.
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)


print(array)
quick_sort(array, 0, len(array)-1)
print(array)

"""
위는 대략적으로 판단하면
예를들어 길이가 N 이면

깊이는
N / 2^k = 1 이 만족하는 k를 생각할 수 있다. [대충 한번 내려갈때마다 반으로 나눈다고 할때 k번 내려가면 2^k만큼 나눌것이고, 이 값이 원소 한개. 즉 1일 것이다.]
그래서 이때 k는 logN 수준

각 순환호출에 대해서 비교연산은 N번정도 할 것이다.

그래서 평균적으로 O(NlogN) 형태이다.


하지만, 이미 정렬되어 있다면 어떨까.
첫번쨰 pivot을 정해서 적절한 위치에 배치된다고 하더라도
맨 왼쪽을 그대로 유지할 것이다.
즉 나머지 부분을 다시 순환호출할 것인데. 이는 단순히 N개의 원소에서 pivot부분을 제외한 N-1개의 원소를 다시 호출하는 경우다.
그러면 횟수는
N + N-1 + N-2 + ... + 1 
= N(N-1)/2 이므로
O(N^2) 형태이다. [최악의 경우를 말이다.]


파이썬 라이브러리는 O(NlogN)을 가능하면 만족하도록
여러 로직을 추가해둔 형태이다.(C++은 일단 퀵정렬을 기반으로 하는데, 다른 로직을 추가해 최악의 경우에도 O(NlogN)가 되도록 했다.)
책에서는 O(NlogN)을 보장하는 형태라고 작성되었다.
"""
