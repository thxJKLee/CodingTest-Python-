import numpy as np
print()
array = []
for i in range(20):
    if i % 2 == 1:
        array += [i]  # array.append(i)
print(f"array >> {array}")

array = [i for i in range(20) if i % 2 == 1]
print(f"[i for i in range(20) if i % 2 == 1] >> {array}")

array = [i*i for i in range(20) if i % 3 == 0]
print(f"[i*i for i in range(20) if i % 3 == 0] >> {array}")

print()

array = [[0] * 4 for _ in range(3)] 
# 중요한 점은 [[0] * m] * n 으로 하면 안된다는 점
# 왜냐하면 리스트끼리 같은 객체로 인식하기 때문.
print("[[0] * 4 for _ in range(3)] >> ")
print(f"3 * 4 배열 >> \n{np.array(array)}")


