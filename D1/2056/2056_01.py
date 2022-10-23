# 2056. 연월일 달력

T = int(input())

for i in range(1,T+1):
    num = str(input())
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    Y = int(num[0:4])
    M = int(num[4:6])
    D = int(num[6:8])
    
    print('#'+str(i), end=' ')
    if (1 <= M <= 12 and 1 <= D <= day_list[M-1]):
        print('%04d/%02d/%02d'%(Y,M,D))
    else:
        print(-1)
