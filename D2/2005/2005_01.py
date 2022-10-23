# 2005. 파스칼의 삼각형 <D2>

def fac(k):
    val = 1
    for i in range(1,k+1):
        val *= i
    return val

def com(n, r):
    return (fac(n)//(fac(r)*fac(n-r)))


N = int(input())
for i in range(1,N+1):
    n = int(input())
    
    print('#'+str(i))
    for j in range(0,n):
        for i in range(0, j+1):
            if j == 0:
                print('1', end=' ')
            else:
                print(com(j,i), end=' ')
        print('')