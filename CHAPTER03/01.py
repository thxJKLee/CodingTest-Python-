import time

N = int(input("거스름돈 >> "))

start_time = time.time()

coin = [500, 100, 50, 10]
count = {500: 0, 100: 0, 50: 0, 10: 0}

for i in coin:
    count[i] = N//i
    print(f"{i:>4d}원: {count[i]:<4d}")
    N = N % i


print(f"손님이 받을 최소 동전의 개수 >> {sum(count.values())}")

end_time = time.time()
print("time: ", end_time-start_time)
