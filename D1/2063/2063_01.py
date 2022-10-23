# 2063. 중간값 찾기

N =  int(input())

num = list(map(int, input().split()))
num.sort()
print(num[(len(num)-1)//2])