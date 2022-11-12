import heapq


def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# 위에는 최소힙인데 최대힙으로 만드는 트릭
# 위에걸 하고 reverse 해도 되지만

def heapsort_MaxHeap(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort_MaxHeap([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 또는

result = heapsort([1,3,5,7,9,2,4,6,8,0])
result.reverse()
print(result)
