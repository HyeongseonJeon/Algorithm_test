# 2001. 파리 퇴치 <D2>

def fun(N_arr, N, M):
    sum_max = -1
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_val = 0
            for k in range(M):
                for l in range(M):
                    sum_val += N_arr[i+k][j+l]
                    if sum_val > sum_max :
                        sum_max = sum_val
    return sum_max

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        num = list(map(int, input().split()))
        arr.append(num)

    print('#'+str(t+1), fun(arr, N, M))