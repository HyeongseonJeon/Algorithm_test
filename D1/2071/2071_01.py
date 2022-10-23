# 2071. 평균값 구하기 <D1>

T = int(input())

for t in range(1, T+1):
    num = list(map(int, input().split()))
    avg = 0
    for i in num:
        avg = sum(num)/len(num)
    print('#'+str(t),round(avg)) # round 반올림