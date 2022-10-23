# 1984. 중간 평균값 구하기 <D2>

T = int(input())


for t in range(1,T+1):
    avg = 0
    num = list(map(int, input().split()))
    num.remove(min(num))
    num.remove(max(num))
    
    avg = round(sum(num)/len(num))
    
    print('#'+str(t), avg)