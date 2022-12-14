"""
계수정렬

데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때.

카운팅 방식으로 해서 메모리공간을 무진장 많이 쓰는 형태이다.
arr 이라는 배열이 있을때 [0으로 초기화된 상태]

정수를 만나는데 이 정수가 a b c d ... z 라고 하자.

그러면 a를 만나면 arr[a]++
b를 만나면 arr[b]++
...
이러면 중복된것도 여러번 만날 수도 있다.

아무튼 데이터의 끝까지 모두 카운트가 완료되면

arr[0]부터 순서대로
갯수만큼 출력하면 된다.

예를들어 arr = [3,2,1,2,0,1,1] 이라면
0 0 0 1 1 2 3 3 5 6 이런식으로 말이다. [아마 코딩도 쉬울 것이다.]
"""
# 이번에는 일반적인 정수의 경우다.
array = [7, -5, 9, 0, 3, 1, 6, 2, -9, 1, 4, 8, 0, 5, -2]

count = [0]*(max(array)-min(array)+1)

for i in range(len(array)):
    count[array[i]-min(array)] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(f"{i+min(array):2d}", end=' ')


"""
그러면 시간복잡도는 어떻게 될까.
공간은 좀 많이 쓰는 느낌이다.

최소값이 단순히 0인경우
데이터의 개수를 N.
데이터의 최대값을 K라고 하면
O(N+K) 수준이다.

즉 데이터인 array를 한번 순회.
그리고 뒤의 for문은 count를 한번 순회 * count의 각각 원소를 순회
즉 N정도와
최대값 K는 곧 count의 배열의 길이. 동시에 sum(count)를 할 경우 N이므로

아무튼 공간상의 제약이 있을 수 있음. 일반적으로 0점~100점 수준의 작은 데이터라면
단순히 크기가 101인 배열을 생성하면 그만이기 때문이다. 하지만 100,000,000 개 수준이라면 배열의 크기가 많이 부담스럽다.


그리고 이제 계수정렬 말고

기수정렬이 있는데
간단히 설명하면 자릿수마다 비교해서 정렬하는데.
모든 자릿수 다 적용하는 것.
대충 O(kN) 수준이다. 이때 k는 제일 큰 수의 자릿수, N은 데이터의 크기
"""