# 2068. 최대수 구하기 <D1>

T = int(input())

for t in range(1, T+1):
    num = list(map(int, input().split()))
    print('#'+str(t),max(num))