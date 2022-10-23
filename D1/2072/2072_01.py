# 2072. 홀수만 더하기 <D1>

T = int(input())

for t in range(1,T+1):
    num = list(map(int, input().split()))
    sum = 0
    for i in num:
        if i%2 == 1:
            sum += i
    print('#'+str(t),str(sum))