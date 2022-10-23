# 2027. 대각선 출력하기 <D1>
# replace 해결 X
from dataclasses import replace


for i in range(5):
    S = '+++++'
    S = replace(S[i], '#')
    print(S)