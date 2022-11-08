print()

a = [1, 4, 3]
print(f"[1, 4, 3] >> {a}")

a.append(2)
print(f"a.append(2) >> {a}")

a.reverse()
print(f"a.reverse() >> {a}")

a.sort()
print(f"a.sort()>> {a}")

a.sort(reverse=True)
print(f"a.sort(reverse=True) >> {a}")

a.insert(3, 9)
print(f"a.insert(3, 9) >> {a}")  # index가 3인 자리에 9를 삽입

print(f"a.count(1) >> {a.count(1)}")

a = [1, 1, 1, 1, 2, 3, 4]
print(f"a >> {a}")
a.remove(1)  # 하나만 제거
print(f"a.remove(1) >> {a}")

print()

remove_set = {1, 2}  # 리스트 remove를 여러개, 혹은 항목 전체를 제거하고 싶을 경우
result = [i for i in a if i not in remove_set]
print(f"[i for i in a if i not in remove_set] >> {result}")

print()
print(f"{a}")
a.extend([1, 2, 3, 4, 5]) # extend의 경우 겉 껍질을 벗긴다음에 추가해주는 방식
print(f"a.extend([1, 2, 3, 4, 5]) >> {a}")
