# 1859. 백만 장자 프로젝트 <D2>

T = int(input())

for i in range(1,T+1):
    money = 0
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = -1

    for j in reversed(range(n)):
        if(max_num < arr[j]):
            max_num = arr[j]
            
        if arr[j] < max_num:
            money += max_num - arr[j]
            
    print('#'+str(i) + ' '+ str(money))