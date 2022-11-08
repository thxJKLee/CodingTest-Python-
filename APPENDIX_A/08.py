data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a | b)
print(a & b)
print(a - b)


data = {1, 2, 3}
print(data)

data.add(4)  # 리스트의 append
print(data)

data.update([5, 6])  # 리스트의 extend
print(data)

data.remove(3)  # 리스트와 동일
print(data)

data = list(data)
data.append(3)
data = set(data)  # 만약 add 를 까먹었다면.
print(data)

data = list(data)
data.extend([7, 8, 9])
data = set(data)  # 만약 update 를 까먹었다면.
print(data)
