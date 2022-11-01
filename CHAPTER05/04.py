"""
팩토리얼

재귀적 vs 반복적
"""


def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1: # 가능하면 == 보다 <= 같이 범위형식으로 재귀탈출하는게 좋다.
        return 1
    return n * factorial_recursive(n-1)


print("반복적 >>", factorial_iterative(10))
print("재귀적 >>", factorial_recursive(10))
