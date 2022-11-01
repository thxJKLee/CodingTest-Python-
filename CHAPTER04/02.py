"""
정수 N 입력
00시 00분 00초 ~
N시 59분 59초

모든 시각중에 3이 하나라도 포함되는 모든 경우의 수

N은 0 ~ 23
"""

N = int(input())  # 0 ~ 23

count = 0

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in (set(str(h)) | set(str(m)) | set(str(s))):
                count += 1

print(count)
