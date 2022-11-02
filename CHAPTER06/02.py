"""
삽입정렬

1. 맨 처음 원소는 정렬되어 있다고 친다.
2. 그 다음 원소부터 확인하는데 정렬되어 있는부분에서 알맞은 위치에 넣는다.
3. 이를 끝까지 사용한다.
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):  # 대입하고 싶은 값은 array[1] 부터 끝까지
    for j in range(i):  # 왼쪽에 이미 정렬된 배열하고 비교해야 하므로 확인할 필요 있음.
        if array[j] >= array[i]:
            # 이미 정렬된 배열에서 순환하고 있던 원소값이 사이에 충분히 들어갈 수 있으면
            temp = array[i]  # array[i]값은 일단 나중에 넣을 것이니깐 메모리 공간을 써서 저장
            for k in range(j, i):  # array[j+1:i] = array[j:i-1] 를 하는 부분
                array[i+j-k] = array[i+j-k-1]
            array[j] = temp  # 마지막에 넣고 싶던 위치에 값을 넣으면 그만
            break  # 뒤에 연산은 굳이 할 필요 없으므로 break로 탈출

print(array)
