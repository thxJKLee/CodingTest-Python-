"""
다시 돌고 돌아 정렬 라이브러리다.

sorted(리스트)
형식으로 진행하면 된다.

혹은
리스트.sort()
로 해줘도 된다.


또한 sorted 나 sort를 진행할때 매개변수로 key 값을 활용할 수있는데.

lambda 식으로 하거나 그냥 함수도 된다.
하지만 lambda 식으로 기억해두고 이를 함수로 치환하는법을 배우는게 편하다.
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)
