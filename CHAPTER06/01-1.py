"""
선택 정렬.
가장 작은값 or 큰값을 찾아서. 앞에 가져다 둔다.
이를 반복한다.

수행횟수는 
처음에는 비교 N번후 앞에 가져다두기
그다음은 비교 N-1번후 앞에 가져다두기
...
마지막에 비교 1번후 앞에 가져다두기.

즉 N + N-1 + N-2 + ... + 2 + 1
= N(N+1)/2
=> O(N^2)

너무 정직하게 N^2 수준으로 걸리기 때문에 적은 데이터에서만 쓰이는 편.
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]

print(array)
