# 1979. 어디에 단어가 들어갈 수 있을까

T = int(input())

for t in range(1,T+1):
    N, K = map(int, input().split())
    
    arr = []
    for n in range(0,N):
        num = list(map(int, input().split()))
        arr.append(num)
    
    row = []
    col = []
    
    rS = 0
    cS = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            
            if arr[i][j] == 1:  # 좌->우
                rS += 1
            else:
                if rS == K:
                   cnt += 1 
                rS = 0
                
            if arr[j][i] == 1:  # 상 -> 하
                cS += 1
            else:
                if cS == K:
                   cnt += 1 
                cS = 0    
                
        if rS == K:
            cnt += 1
        if cS == K:
            cnt += 1 
        rS, cS = 0, 0
    print('#'+str(t), cnt)