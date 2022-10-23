# 2058. 자릿수 더하기

sum_val = 0

num = int(input())
for i in str(num):
    sum_val += int(i)

print(sum_val)