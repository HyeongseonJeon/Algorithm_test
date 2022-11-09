# 1285. 아름이의 돌 던지기 <D2>

T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    arr = [abs(num) for num in numbers]
    print('#'+str(t), min(arr), arr.count(min(arr)))