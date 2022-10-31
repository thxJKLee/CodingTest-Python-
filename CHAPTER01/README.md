# 복잡도

`알고리즘의 성능을 나타내는 척도`

|                 |                                    |
| --------------: | :--------------------------------- |
| **시간 복잡도** | 알고리즘을 위해 필요한 연산의 횟수 |
| **공간 복잡도** | 알고리즘의 위해 필요한 메모리의 양 |

1. 시간 복잡도 : 얼마나 오래 걸리는가.
2. 공간 복잡도 : 얼마나 많이 자원을 소모하는가.
    - 물론, 메모리를 넉넉하게 써서 시간을 대폭줄이는 방식이 있음
        - 메모이제이션 Memoization
        - 뭐 간단한 예시로, 자주 나오는 값이라면 필요할때마다 연산하기 보다는, 그냥 값으로 저장하는게 연산하기 편한듯

<hr>

## 시간 복잡도

<hr>

대표적으로 다음과 같은 big-O함수 형태를 가진다.
<br>[정확한 시간은 다를지 몰라도, 대체로 저러한 시간을 가진다 라고 생각하면 된다.]

1. _O(1)_
    - 상수 시간
2. _O(N)_
    - 선형 시간
3. _O(N<sup>2</sup>)_
    - 이차
4. _O(N<sup>3</sup>), ..., O(N<sup>k</sup>)_ 등
    - 삼차, ..., k차
    - 이러한 것들을 다항 시간 이라고 표현한다.
5. _O(logN)_
    - 로그 시간
6. _O(NlogN)_
    - 로그 선형 시간
7. _O(2<sup>n</sup>)_
    - 지수 시간

예를 들면 아래와 같음

```python
# 시간 복잡도 : O(N)
array = [3, 5, 1, 2, 4]
summary = 0

for x in array:
    summary += x
print(summary)
```

```python
# 시간 복잡도 : O(1)
a = 5
b = 7
print(a + b)
```

```python
# 시간복잡도 : O(N^2)
array = [3, 5, 1, 2, 4]

for i in array:
    for j in array:
        temp = i * j
        print(temp)
```

추가로 알아두면 좋은 점이 for문이 시간 복잡도의 완벽한 척도는 아님.
<br>내부에서 다른 함수를 호출한다던가
<br>일부 행동은 그냥 통과된다던가

또한, 상수부분을 완전히 무시하는것도 위험한 행동이다.
<br>상수부분이 10억이라면 충분히 영향력이 클 것이다.

코딩테스트에서는 연산횟수가 10억정도로 크게 된다면 오답판정을 받기 때문에
<br>_O(N<sup>3</sup>)_ 이상으로는 안되는 편이 좋다.

<hr>

| N의 범위          | 시간복잡도                |
| ----------------- | ------------------------- |
| \< **500**        | \< **_O(N<sup>3</sup>)_** |
| \< **2,000**      | \< **_O(N<sup>2</sup>)_** |
| \< **100,000**    | \< **_O(NlogN)_**         |
| \< **10,000,000** | \< **_O(N)_**             |

물론 최대한 빠른 시간이 좋겠지만, 이정도여도 가능하다고 생각하면 좋을 듯 하다.

<hr>

## 공간 복잡도

<hr>

기본적으로 big-O 표기법을 따른다.
<br>또한, 코테에서는 메모리 사용량 **128MB** 제한이라는 형식으로 명시되어 있다.
<br>[보통 **128MB** ~ **512MB**]
<br>결론은, 리스트의 크기를 1000만단위 수준으로 크게 만들면 많이 곤란해진다.

다음은 int를 기준으로 리스트 크기에 따른 메모리 사용량이다.

|                    | 용량     |
| ------------------ | -------- |
| int a[1000]        | **4KB**  |
| int a[1000000]     | **4MB**  |
| int a[2000][2000]  | **16MB** |
| int a[10000000000] | **4GB**  |

보통은 아래처럼 수행시간을 측정할 수 있다.
<br>시간

```python
import time
start_time = time.time()

"""
소스 코드 구역
"""

end_time = time.time()
print("time: ", end_time-start_time)
```

-   01.py

    -   _O(N)_

-   02.py

    -   _O(1)_

-   03.py

    -   _O(N<sup>2</sup>)_

-   04.py

    -   시간 측정
    -   주로 공부할 때
    -   이미 만들어진 라이브러리와 속도를 비교하고 싶을 때 사용

-   05.py

    -   직접 만든 정렬 (선택정렬) 의 시간 측정
    -   대략 12초 정도 걸린다. [어쨋든 오래걸린다.]

-   06.py
    -   파이썬 기본 정렬 라이브러리의 시간 측정
    -   심지어 0초로 측정되는 경우도 있을정도로 빠르다.