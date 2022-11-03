"""
보면 알겠지만
fibo(3) 부분이 여러번 나오곤 함.

이 반복적으로 나오는걸 아래처럼 하면 반복자체를 막을 수 있음

아래의 경우는 큰문제를 해결하기 위해
작은 문제를 호출하므로
이를 탑다운(메모이제이션) 방식이라고 함.
"""
fibo_arr = [0] * 100


def fibo(x):
    print(f"f({str(x)})", end=" ")
    if x == 1 or x == 2:
        return 1
    if fibo_arr[x] != 0:
        return fibo_arr[x]
    fibo_arr[x] = fibo(x-1) + fibo(x-2)
    return fibo_arr[x]


print(fibo(6))
"""
차례대로 살펴보자.

fibo(6) : fibo_arr[6] = fibo(5) + fibo(4)
    
    fibo(5) : fibo_arr[5] = fibo(4) + fibo(3)
        
        fibo(4) : fibo_arr[4] = fibo(3) + fibo(2)
            
            fibo(3) : fibo_arr[3] = fibo(2) + fibo(1)
                fibo(2) : return 1
                fibo(1) : return 1
                
            => fibo_arr[3] = 1 + 1 = 2
            => return fibo_arr[3] = 2
            
            fibo(2) : 1
            
        => fibo_arr[4] = 2 + 1 = 3
        => return fibo_arr[4] = 3
        
        fibo(3) : fibo_arr[3] != 0
        => return fibo_arr[3] = 2
        
    => fibo_arr[5] = 3 + 2 = 5
    
    fibo(4) : fibo_arr[4] != 0
    => return fibo_arr[4] = 3

=> fibo_arr[6] = 5 + 3 = 8
=> return fibo_arr[6] = 8

이미 계산이 완료된 값은
if문에서 탈출해서 계산을 포기한다.
그리고 그 값을 써야 한다면 그 index 부분의 값을 끄집어 오면 된다.
"""

"""
다이나믹 프로그래밍에서는 다음과 같은 조건에서만 사용가능하다.
1. 큰 문제를 작은 문제로 나눌 수 있을 것
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일할 것
"""
