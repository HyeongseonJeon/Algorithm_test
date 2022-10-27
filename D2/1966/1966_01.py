# 1966. 숫자를 정렬하자 <D2>

T = int(input())

for T in range(1,T+1):
    
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()
        
    print('#'+str(T), end=' ')
    for i in num:
        print(i, end=' ')
    print()