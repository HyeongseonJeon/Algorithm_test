# 1936. 1대1 가위바위보 <D1>

# 가위 1 | 바위 2 | 보 3

A, B = map(int, input().split())

# A가 이기는 경우 1 3 | 3 2 | 2 1
# A가  지는 경우  1 2 | 3 1 | 2 3 

if A < B: A + 3

if A - B == 1: print('A')
else: print('B')