"""
다이나믹 프로그래밍
동적 계획법

메모리 공간을 약간 더 사용해서 연산속도를 올리는 방법

1. 탑다운 방식
2. 보텀업 방식
"""

"""
예를들어 피보나치 수열을 생각해보자.
기본 식은 다음과 같다.
f(1) = 1
f(2) = 1
f(n+2) = f(n+1) + f(n) (n>=1, n은 정수)
"""


def fibo(x):
    print(f"fibo({x})", end=" ")
    if x == 1 or x == 2:
        print()
        return 1
    return fibo(x-1)+fibo(x-2)


print(fibo(6))
