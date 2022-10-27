# 1961. 숫자 배열 회전 <D2>

# Up(역), Left(역), Down(순)의 방향으로 규칙 => reversed 순 : False, 역 : True
# first Col(순), last Row(역), last Row(역)부터 시작 => 순 : i, 역 : -(i+1)
def Rotaion(Row, Col):
    for i in range(len(Row)):   # len(Row) == len(Col)
        print(*reversed(Col[i]), sep ='', end=' ')      #print(*list) => '[]'없이 원소들 출력, sep='' 구분
        print(*reversed(Row[-(i+1)]), sep ='', end=' ')
        print(*Col[-(i+1)], sep ='')
        
T = int(input())

for t in range(1,T+1):
    N = int(input())
    row_arr = []    # 행 생성
    col_arr = []    # 열 생성
    for n in range(N):
        num = list(map(int, input().split()))
        row_arr.append(num) 
    
    
    for n in range(N):
        col = [row[n] for row in row_arr]   # 열 추출
        col_arr.append(col)     # 열 배열 생성
        
    # print('Row', row_arr)
    # print('Col', col_arr)
    print('#'+str(t))
    Rotaion(row_arr, col_arr)