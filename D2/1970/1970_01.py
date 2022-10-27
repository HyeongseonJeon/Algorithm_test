# 1970. 쉬운 거스름돈 <D2>

def change(target):
    money = [50000, 10000, 5000, 1000, 500, 100, 50 ,10]
    number = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(len(money)):
        number[i] = target // money[i]
        target = target % money[i]
        
    return number

T = int(input())

for t in range(1, T+1):
    target = int(input())
    
    print('#'+str(t))
    for i in change(target):
        print(i, end=' ')
    print()
