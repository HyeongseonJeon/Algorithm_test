# 2070. 큰 놈 , 작은 놈 , 같은 놈 <D1>

T = int(input())

for t in range(1, T+1):
    num = list(map(int, input().split()))
    if num[0] < num[1]:
        s = '<'
    elif num[0] > num[1]:
        s = '>'
    else:
        s = '='
    print('#'+str(t),s)