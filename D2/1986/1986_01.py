# 1986. 지그재그 숫자 <D2>

T = int(input())

for t in range(1,T+1):
    
    N = int(input())
    
    sum_val = 0
    for n in range(1,N+1):
        
        if n % 2 == 0:
            n = -n
        
        sum_val += n
    print('#'+str(t), sum_val)        
            