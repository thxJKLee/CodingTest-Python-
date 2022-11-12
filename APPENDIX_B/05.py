"""
구간 합 계산.

일반적인 경우라면.
M개의 쿼리요청이 있고,
그 요청에 대해 최대 N개의 숫자까지(즉 리스트 전체)
합해야 할 수도 있기 때문에
O(NM) 수준이다.

그래서 여기서는
접두사 합을 이용하여 구간합을 빠르게 계산한다.
1. N개의 수에 대하여 접두사 합을 게산하여 배열 P에 저장한다.
2. 매 M개의 쿼리정보 [L, R]을 확인할때 구간합은 P[R] ~ P[L-1]

즉,
미리 0번부터 x번까지 구간합을 저장한다.
이는 O(N) 수준

그러면 0 , 0~0, 0~2, ... 0~n 
[맨 처음에 None 느낌으로 값이 있는 이유는 뒤에 연산때문에.]

그리고 left 부터 right까지 합을 계산하고 싶다면
P[right] - P[left-1] 을 해주면 그만이다. 이는 O(1)이다.
    0~right
-   0~left-1
-------------
    left~right


다만 이러한 쿼리가 M개 있을 수 있으므로
전체적인 횟수는 O(N+M)이 될 것이다.
"""
n = 5
data = [10, 20, 30, 40, 50]
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 2
right = 3
print(prefix_sum[right]-prefix_sum[left-1])
"""
prefix_sum[0]가 0으로 미리 설정해둔 이유는 계산을 통일하기 위해서

예를들어 0부터 n까지 합치고 싶다면
prefix_sum[n] - prefix_sum[0]

1부터 n까지 합치고 싶다면
prefix_sum[n] - prefix_sum[1]
"""
