def Sum(i):
    if i==1:
        return 1
    else:
        return i+Sum(i-1)
# print(Sum(5)) # 15
print('i=',end='')
i=int(input())
print(Sum(i))