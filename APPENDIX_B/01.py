import time
start_time = time.time()
"""
소수의 판별에 대해
일반적으로 제일 쉬운방법
"""


def is_prime_number(x):
    for i in range(2, x):  # 2 ~ x-1 까지 x에서 나누는데. 나머지가 0인 경우가 발생하면
        if x % i == 0:
            return False
    return True


for i in range(2, 20):
    print(f"{i:<6d}|", end=' ')
print()
for i in range(2, 20):
    print(f"{str(is_prime_number(i)):6s}|", end=' ')
print()
"""
최대로 오래걸린다면 분명
O(X) 시간 정도 걸릴 것이다.

정수론을 상기시키면 되는데.
결론만 말하자면
    => 굳이 다 확인할 필요 없이. 절반수준만 확인하면 되지 않을까?

예를 들어 16이라고 하자.
01 * 16 = 16
02 * 08 = 16
04 * 04 = 16
[여기는 굳이 할 필요 없다.]
[여기도 굳이 할 필요 없다.]

즉, 
숫자 X가 있다면.
sqrt(X) 까지만 확인해도 더이상 확인할 필요가 없다.
그러면 시간복잡도는 O(sqrt(X)) 수준이 된다.
"""

for i in range(2,20000):
    is_prime_number(i)
    
end_time = time.time()
print("time: ", end_time-start_time)
