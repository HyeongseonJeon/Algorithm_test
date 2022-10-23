# 2001. 파리 퇴치 <D2>

def fun(N_arr, N, M):
    sum_max = -1
    sum_val = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_val = int(N_arr[i+0][j+0]) + int(N_arr[i+0][j+1]) +\
                      int(N_arr[i+1][j+0]) + int(N_arr[i+1][j+1])
            if sum_val > sum_max :
                sum_max = sum_val
    return sum_max

T = int(input())

N, M = map(int, input().split())


arr = []
for t in range(T):
    for i in range(N):
        num = list(map(int, input().split()))
        arr.append(num)

    print('#'+str(t+1), fun(arr, N, M))