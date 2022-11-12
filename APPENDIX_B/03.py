"""
투 포인터

리스트에 순차적으로 접근해야할 때 2개의 점 위치를 기록하면서 처리하는 알고리즘
굳이 얘기하면 슬라이싱처럼 1번부터 7번까지. 이런식으로 처리하고 싶을 경우에 사용한다.

예를 들어 특정 리스트를 슬라이싱 했을 때, 특정한 합인 수열이 몇개인지 출력한다고 하자.
1. start가 0, end를 0 으로. index=0 을 가리키도록 하자
2. 현재 부분합이 M과 같다면 count++
3. 현재 부분합이 작다면 end++
4. 현재 부분합이 크거나 같으면 start++
5. 모든 경우를 확인할때까지


일반적으로 iterator의 경우를 생각하면 포인터가 하나뿐이라고 생각할 수 있는데
이 iterator를 두개를 두고 생각하면 될 듯
"""
#
n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
