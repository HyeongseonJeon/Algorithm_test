# 1954. 달팽이 숫자 <D2>

def print_snail(N):
    
    # 차례대로 Right, Down, Left, Up
    dr = [0, 1, 0, -1]  # 행 이동
    dc = [1, 0, -1, 0]  # 열 이동
    
    arr = [[0]*N for _ in range(N)]
    d = 0       # 방향 벡터
    row = 0     # 행 좌표
    col = 0     # 열 좌표
    for i in range(1, N**2+1):
        arr[row][col] = i   # 숫자 대입
        
        if  row+dr[d] < 0 or row+dr[d] > (N-1) or \
            col+dc[d] < 0 or col+dc[d] > (N-1):     # 벽에 부딪힌 경우
            d = (d+1) % 4   # 방향을 바꿈
        elif arr[row+dr[d]][col+dc[d]] != 0:  # 다음 숫자가 0이 아닌경우
            d = (d+1) % 4   # 방향을 바꿈
            
        row += dr[d]    # 행 좌표 변경
        col += dc[d]    # 열 좌표 변경
    for x in arr:
        print(*x, sep=' ')
        

T = int(input())

for t in range(1,T+1):
    N = int(input())
    print('#'+str(t))
    print_snail(N)
        