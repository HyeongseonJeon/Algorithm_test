# 1859. 백만 장자 프로젝트 <D2>
# 재귀 함수로 풀이 - No

global sum_val
sum_val = 0

def fun1(num):
    for i in (range(len(num))):
        if i+1 == len(num):
            break 
        if num[-1] > num[-i-2]:
            sum_val += num[-1] - num[-i-2]
        else:
            del num[-(i+1):]
            fun1(num)   
            
T = int(input())

for t in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    
    fun1(num)
    
    print('#'+str(t), sum_val)