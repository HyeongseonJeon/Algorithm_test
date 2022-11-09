# 1945. 간단한 소인수분해 <D2>

T = int(input())

prime_factors = [2, 3, 5, 7, 11]
answer = [0, 0, 0, 0, 0]
for t in range(1,T+1):
    num = int(input())

    for i in range(5):
        cnt = 0
        while num % prime_factors[i] == 0:
            num = num / prime_factors[i]
            cnt += 1
        answer[i] = cnt

    print('#'+str(t), *answer)