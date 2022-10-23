# 1989. 초심자의 회문 검사 <D2>

T = int(input())

for t in range(1,T+1):
    k = 0
    S = str(input())
    if S == S[::-1]:
        k = 1
    
    print('#' + str(t), k)