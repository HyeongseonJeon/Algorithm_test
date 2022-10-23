# 2029. 몫과 나머지 출력하기 <D1>

T = int(input())
for i in range(1,T+1):
    k1, k2 = map(int, input().split())
    print('#'+str(i), k1//k2, k1%k2)