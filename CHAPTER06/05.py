"""
기본 정렬 라이브러리로 sorted() 함수를 제공함.
병합정렬을 기반으로 만들어 졌음.
일반적으로 퀵정렬보다 느리지만, 최악의 경우에도 O(NlogN) 수준

그러면 일단 병합정렬을 대강 설명하는 편이 좋을 듯

기본원리
1. 배열을 충분히 나누어 각각 1개의 원소만 되도록 한다.
2. 인접한 배열은 합한다. 합할때는 새로운 배열이 생성되도록 하는데 정렬이 이루어진다.
3. 2번을 원래 배열 크기가 되도록 합치면, 그게 곧 정렬이 이루어진 방식이다.

구현방식
1. left 부터 right 까지 합병정렬을 한다고 하자.
2. 그러면 순환구조로 left ~ mid 부분의 합병정렬과 mid+1 ~ right 부분의 합병정렬도 진행한다.
3. 그리고, 실제로 합병하는 과정인 merge도 따로 구현하는데. 여기는 left ~ mid ~ right 까지 받아올 것이다.
4. 합병의 경우 left ~ mid ~ right 까지 크기를 가지는 배열을 선언한다.
0 ~ right-1 일텐데.
left~mid 배열과
mid+1~right 배열의 원소를 왼쪽부터 비교해서 작은걸 새로운 배열의 맨 왼쪽 원소로 함.

5. 4번을 계속 반복한다. 그러면 left~mid~right 까지 정렬되며 합쳐질 것이다.
"""
array = [27, 10, 12, 20, 25, 13, 15, 22]


def merged_sort(arr, left, right):
    if left == right:
        return
    mid = (left+right)//2  # 기준점을 정하는 과정. 분할
    merged_sort(arr, left, mid)  # 앞쪽 부분도 합병정렬. 정복
    merged_sort(arr, mid+1, right)  # 뒤쪽 부분도 합병정렬. 정복
    merge(arr, left, mid, right)  # 앞 뒤 정렬되어 있을텐데, 이를 실제로 합병하는 과정. 결합


def merge(arr, left, mid, right):
    tmp = [0]*(right-left+1)
    # 크기가 left ~ right 까지 되는 배열
    k = 0
    # left~mid 배열과, mid+1~right 배열이 있겠지.
    # 각각 A 배열, B 배열이라고 하자.
    i = left
    j = mid+1
    
    # A배열의 첫번째 원소와 B배열의 첫번째 원소를 비교해 작은 값을 tmp배열의 첫번째 부터 넣는다.
    # 넣어진 값이 A 배열에 있다면 A배열은 다음 원소로 넘어가고
    # 넣어진 값이 B 배열에 있다면 B배열은 다음 원소로 넘어간다.
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i += 1
            k += 1
        else:
            tmp[k] = arr[j]
            j += 1
            k += 1
    
    # 위의 과정을 하다보면 남은 원소들이 A배열이든 B배열이든 있을 것이다.
    # A배열이 남은 경우와, B배열이 남은 경우. 나머지 부분은 비교하지말고 곧장 tmp배열에 넣어버린다.
    if i > mid:
        while j <= right:
            tmp[k] = arr[j]
            j += 1
            k += 1
    else:
        while i <= mid:
            tmp[k] = arr[i]
            i += 1
            k += 1

    # 이제 arr[left]에 tmp[0]의 값을 넣고 싶고
    # 쭉쭉 가서
    # arr[right]에 tmp[left-right] 를 넣고 싶은거니깐.
    # 이를 아래에서 진행해준다.
    i = left
    for x in tmp:
        arr[i] = x
        i += 1


merged_sort(array, 0, len(array)-1)

print(array)
