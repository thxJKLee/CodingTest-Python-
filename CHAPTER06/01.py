array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min = i
    for j in range(i+1, len(array)):
        if array[min] > array[j]:
            min = j
    temp = array[min]
    array[min] = array[i]
    array[i] = temp
    # 스왚은 사실 파이썬의 튜플 방식을 이용하면 좋다.

print(array)
