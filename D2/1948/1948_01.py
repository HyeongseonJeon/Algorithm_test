# 1948. 날짜 계산기 <D2>

T = int(input())

List_Month = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
List_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, T+1):
    M1, D1, M2, D2 = map(int, input().split())
    answer = sum(List_day[M1:M2]) + D2 - D1 + 1
    print('#'+str(t), answer)