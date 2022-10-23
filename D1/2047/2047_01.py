# 2047.신문 헤드라인 <D1>

ch = str(input())

for c in str(ch):
    if(97 <= ord(c) <= 122):
        print(chr(ord(c)-32), end='')
    else:
        print(c, end='')