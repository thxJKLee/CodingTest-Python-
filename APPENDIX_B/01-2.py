# 1부터 1,000,000 까지 모든 소수 출력
import time
start_time = time.time()

def is_prime_number(x):
    for i in range(2,int(x**(1/2))+1):
        if x%i==0:
            return False
    return True

count = 0
for i in range(1,1000000+1):
    if is_prime_number(i):
        count+=1
        
print(count)

end_time = time.time()
print(end_time-start_time)