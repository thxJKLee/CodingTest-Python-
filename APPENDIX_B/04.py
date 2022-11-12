"""
정렬되어있는 두 집합에 대한 두 리스트의 합집합
"""
import random

list01_length = 10
list02_length = 15
list01 = [0 for i in range(list01_length)]
list02 = [0 for i in range(list02_length)]

for i in range(list01_length):
    list01[i] = random.randint(0, 99)
for i in range(list02_length):
    list02[i] = random.randint(0, 99)

list01.sort()
list02.sort()

i = 0
j = 0
k = 0

result = [0 for i in range(list01_length+list02_length)]

while i < list01_length and j < list02_length:
    if list01[i] < list02[j]:
        result[k] = list01[i]
        i += 1
        k += 1
    else:
        result[k] = list02[j]
        j += 1
        k += 1

if i < list01_length:
    result[k] = list01[i]
    i += 1
    k += 1

if j < list02_length:
    result[k] = list02[j]
    j += 1
    k += 1

print(list01)
print(list02)
print(result)
