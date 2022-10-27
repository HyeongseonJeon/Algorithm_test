# 1959. 두 개의 숫자열 <D2>

def Num_str(A,B):
    if len(A) > len(B):
        A,B = B,A   # A가 항상 작거나 같게 형성
        
    tmp = len(B)-len(A)+1   # B-A+1 만큼 반복
    arr = []
    for i in range(tmp):
        mul_AB = [a*b for a,b in zip(A,B[0+i:len(A)+i])]      # A*B 리스트 생성
        arr.append(sum(mul_AB))     # A*B 리시트의 합을 arr에 추가
    return max(arr)
    
T = int(input())

for t in range(1,T+1):
    N, B = input().split()
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    print('#'+str(t), Num_str(Ai, Bi))