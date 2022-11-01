def recursive_function(i):
    if i == 100:
        return
    print(i, "번째 재귀 함수에서", i+1, "번째 재귀 함수를 호출합니다.")
    recursive_function(i+1)  # 재귀함수를 호출하는 부분이 여기에 있기 때문에.
    # 모든 재귀함수가 일단 실행된 다음. 이 다음 문장이 실행된다.
    print(i, "번째 재귀 함수를 종료합니다.")


recursive_function(1)
