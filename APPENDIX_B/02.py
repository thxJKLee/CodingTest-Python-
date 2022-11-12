"""
에라토스테네스의 체
    => 여러 개의 수가 소수인지 아닌지 판별하는 방법
    
기본 방식은 다음과 같다.
1. 2 ~ N 까지 자연수 나열
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다.(i는 제거하지 않음)
4. 반복할 것이 없을때까지 2, 3을 반복한다.

그러면 어떻게 할지 한번 수도코드 느낌으로 해보자.
채에 막히면 False
채에 막히지 않았으면 True
2는 True 이므로
    => 4, 6, 8, 10, ... 을 False 로
3는 True 이므로
    => 6, 9, 12, ... 을 False 로
4는 False 이므로
5는 True 이므로
    => 10, 15, 20, ... 을 False 로
...
"""
import time
start_time = time.time()

n = 100000
array = [True for _ in range(n+1)]

for i in range(2, int(n**(1/2))+1):
    if array[i] == True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

count = 0
for i in range(2, n+1):
    if array[i]:
        print(f"{i:5d}", end=' ')
        count += 1
        if count % 10 == 0:
            print()
print()
print(count)
end_time = time.time()
print(end_time-start_time)

"""
생각보다 if 계산하는건 찰나의 시간만 걸린다고 생각하면 된다.
그래서 이 연산이 속도가 괜찮은 편이다.
물론 공간복잡도는 좀 크긴 하다.
"""