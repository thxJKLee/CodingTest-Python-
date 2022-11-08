print()

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"a >> {a}")

print(f"a[4] >> {a[4]}")
print(f"a[-2] >> {a[-2]}")
print(f"a[len(a) -2] >> {a[len(a) -2]}")
print(f"a[1:3] >> {a[1:3]}")
print(f"a[6:] >> {a[6:]}")
print(f"a[:6] >> {a[:6]}")
print(f"a[:] >> {a[:]}")
print(f"a[1:-2:2] >> {a[1:-2:2]}")  # 1(이상) ~ len(a)-2(미만), step은 2

print()

a = list()
print(f"list() >> {a}")

a = []
print(f"[] >> {a}")

print()

n = 10
a = [0] * n
print(f"[0] * 10 >> {a}")

print()

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[1:3] = [10, 11]
print("리스트는 중간의 값을 변경할 수 있다. 이는 슬라이싱으로 얻은 값이어도 가능하다.")
print("그리고 여러 특정한 타입들과의 변환은 자유로운 편이다.")
print(f"a >> {a}")
print(f"a[1:3] = [10, 11] >> {a}")