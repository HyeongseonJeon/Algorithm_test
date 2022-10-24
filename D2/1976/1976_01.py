# 1976. 시각 덧셈 <D2>

T = int(input())

for t in range(1,T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h3 = (m1+m2)//60
    h = (h1+h2+h3)%12
    if h == 0:
        h = 12
    m = (m1+m2)%60
    print('#'+str(t), h, m)