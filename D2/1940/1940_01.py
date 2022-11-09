# 1940. 가랏! RC카! <D2>

T = int(input())

for t in range(1,T+1):
    N = int(input())
    distance = 0
    speed = 0
    data = []
    for n in range(N):
        data = list(map(int, input().split()))    # c : 커맨드, a : 가속도
        c = data[0]
        if len(data) == 2: a = data[1]
        if c == 1:
            speed += a
        elif c == 2:
            speed -= a
            if speed < 0: speed = 0
        distance += speed

    print('#'+str(t), distance)