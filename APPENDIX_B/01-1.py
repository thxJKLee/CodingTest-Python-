import time
start_time = time.time()
"""
소수의 판별에 대해
개선된 방법
굳이 전체다 확인하는게 아닌
sqrt(X) 까지만 확인해본다.

무려 제곱만큼 차이나므로 시간 차이가 심해진다
"""


def is_prime_number(x):
    # x**(1/2)는 float형이므로 int형으로 바꿀 필요가 있다.
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True


for i in range(2, 20):
    print(f"{i:<6d}|", end=' ')
print()
for i in range(2, 20):
    print(f"{str(is_prime_number(i)):6s}|", end=' ')
print()

for i in range(2, 20000):
    is_prime_number(i)

end_time = time.time()
print("time: ", end_time-start_time)
