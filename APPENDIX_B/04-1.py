import random

n, m = 10, 15
a = [0] * n
b = [0] * m
result = [0]*(n+m)

for i in range(n):
    a[i] = random.randint(0, 200)
for j in range(m):
    b[j] = random.randint(0, 200)

a.sort()
b.sort()

i = 0
j = 0
k = 0
while i < n and j < m:
    if j >= m or (i < n and a[i] < b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end=' ')
