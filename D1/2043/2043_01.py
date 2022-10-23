# 2043. 서랍의 비밀번호 <D1>

P, K = map(int, input().split())

if(P >= K):
    print(P - K + 1)
else:
    print(1000 + P - K + 1)