import random

array = list(range(20))
random.shuffle(array)

print(array)
print(sum(array))
print(min(array))
print(max(array))

result = "(3+5)*7"
print(f"(3 + 5) * 7 = {eval(result)}")

result = sorted(array)
print(result)

random.shuffle(array)
print(result)

result = sorted(array, reverse=True)
print(result)

data = [7, 47, 8, 2]
data.sort()  # return 값 없이 실제 값 자체를 변경.
print(data)

