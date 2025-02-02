num = '14679'
sum = 0
for i in range(len(num)): # range means from 0 to a number-1. and len means the number is the length of num which is 5
    if i % 2 == 0:
        a = 2*  int(num[i])
        b = a // 10
        c = a % 10
        d = b + c
        e = d
    else:
        f = int(num[i])
        e = f
    sum += e
print(sum)

# print(2+4+3+7+9)