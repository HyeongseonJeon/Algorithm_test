# 1859. 백만 장자 프로젝트 <D2>

T = int(input())

for t in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    
    sum_val = 0
    cehck = False
    while len(num) > 1:
        for i in (range(2,len(num)+1)):
            if num[-1] > num[-i]:
                sum_val += num[-1] - num[-i]
            else:
                del num[-(i-1):]
                break
            
            if i == len(num):
                cehck = True
                break
        if cehck:
            break
        
    print('#'+str(t), sum_val)
    
# 시간복잡도를 생각을 잘 해보자 뒤에서 접근하기!