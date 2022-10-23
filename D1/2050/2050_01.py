# 2050. 알파벳을 숫자로 변환

ch = str(input())

for c in str(ch):
    print(ord(c)-64, end=' ')