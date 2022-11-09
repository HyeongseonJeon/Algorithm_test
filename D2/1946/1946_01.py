# 1946. 간단한 압축 풀기 <D2>

T = int(input())

for t in range(1, T+1):
    arr = []
    N = int(input())

    for n in range(1, N+1):
        char, num = map(str, input().split())
        num = int(num)
        for k in range(num):
            arr.append(char)
    print('#' + str(t))
    for k in range(len(arr)):
        print(*arr[k], sep='', end='')
        if (k+1)%10 == 0:
            print("")
    print("")