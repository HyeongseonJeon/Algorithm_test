# 1288. 새로운 불면증 치료법 <D2>

T = int(input())

for t in range(1,T+1):
    N = int(input())
    k = 1
    cnt = 0
    numbers = set()
    while len(numbers) != 10:
        kN= k * N
        str_num = str(kN)
        arr = [element for element in str_num]
        numbers = numbers | set(arr)
        k += 1
    print('#'+str(t), kN)